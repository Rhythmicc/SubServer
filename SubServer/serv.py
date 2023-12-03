import pickle
from . import *
from fastapi import FastAPI
from fastapi.responses import FileResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger


async def _update(airport: str):
    """
    更新配置文件

    :param airport: 机场名
    """
    import pickle

    QproDefaultConsole.print(QproInfoString, "AUTO UPDATE", f"Updating {airport}...")
    header = requirePackage(f'sub_clash.main', 'app', real_name=f'git+https://github.com/Rhythmicc/sub-clash.git').real_call('update', airport, force=True, disable_txcos=True)
    header = header.headers['subscription-userinfo']
    with open(f'{airport}.header', 'wb') as f:
        pickle.dump(header, f)


scheduler = AsyncIOScheduler()
trigger = IntervalTrigger(hours=int(config.select('interval')))
for i in config.select('airports'):
    scheduler.add_job(_update, trigger, args=[i])
serv = FastAPI()


@serv.get("/update")
async def update(airport: str):
    """
    更新配置文件

    :param airport: 机场名
    """
    _update(airport)
    return {"message": "updated"}


@serv.get("/subscribe")
async def subscribe(airport: str):
    """
    获取订阅链接
    """
    with open(f'{airport}.header', 'rb') as f:
        header = pickle.load(f)
    return FileResponse(f'{airport}.yaml', headers={'subscription-userinfo': header})

@serv.on_event("startup")
async def startup():
    scheduler.start()

@serv.on_event("shutdown")
async def shutdown():
    scheduler.shutdown()