import discord
import logging
from logging.handlers import RotatingFileHandler
import contextlib
import asyncio

from bot import EEServ
import parameters
class RemoveNoise(logging.Filter):
    def __init__(self):
        super().__init__(name='discord.state')

    def filter(self, record:logging.LogRecord)->bool:
        if record.levelname == "WARNING" and 'referencing an unknown' in record.msg:
            return False
        return True


@contextlib.contextmanager
def setup_logging():
    log = logging.getLogger()

    try:
        discord.utils.setup_logging()

        max_bytes = 32 * 1024 * 1024 # 32 MB
        logging.getLogger('discord').setLevel(logging.INFO)
        logging.getLogger('discord.http').setLevel(logging.WARNING)
        logging.getLogger('discord.state').addFilter(RemoveNoise())

        log.setLevel(logging.INFO)
        handler = RotatingFileHandler(filename='eeserv.log', encoding='utf-8', mode='w', maxBytes = max_bytes, backupCount=5)
        dm_fmt = "%Y-%m-%d %H:%M:%S"
        fmt = logging.Formatter('[{asctime}] [{levelname:<7}] {name}: {message}', dm_fmt, style='{')
        handler.setFormatter(fmt)
        log.addHandler(handler)

        yield

    finally:
        # exit
        handlers = log.handlers[:]
        for hdlr in handlers:
            hdlr.close()
            log.removeHandler(hdlr)

async def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    log = logging.getLogger()
    param = parameters.load_parameters()
    bot = EEServ(param)


    
    await bot.start_bot()


def main():
    with setup_logging():
        asyncio.run(run_bot())

if __name__ == "__main__":
    main()

