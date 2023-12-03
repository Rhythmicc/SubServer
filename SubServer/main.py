from QuickProject.Commander import Commander
from . import _update
from . import *

app = Commander(executable_name)


@app.command()
def serv(port: int = 8080):
    """
    启动服务器

    :param port: 服务器端口
    """
    from .serv import serv
    from uvicorn import run

    # from apscheduler.schedulers.asyncio import AsyncIOScheduler
    # from apscheduler.triggers.interval import IntervalTrigger

    # scheduler = AsyncIOScheduler()
    # trigger = IntervalTrigger(hours=int(config.select('interval')))
    # for i in config.select('airports'):
    #     scheduler.add_job(_update, trigger, args=[i])
    # scheduler.start()
    # app_startup()

    run(serv, port=int(config.select('port')), host=config.select('host'))

    # scheduler.shutdown()


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == "__main__":
    main()
