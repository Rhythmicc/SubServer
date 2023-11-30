import pickle
from . import *
from . import _update
from fastapi import FastAPI
from fastapi.responses import FileResponse


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
