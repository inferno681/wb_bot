import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import Redis, RedisStorage

from bot.handlers import router
from bot.service import service
from config import config

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

bot = Bot(token=config.secrets.token.get_secret_value())

redis = Redis(
    host=config.redis.host, port=config.redis.port, db=config.redis.redis_db
)
storage = RedisStorage(redis=redis)

dp = Dispatcher(storage=storage)
dp.include_router(router)


async def main() -> None:
    try:
        logger.info('Starting bot...')
        await dp.start_polling(bot)
    finally:
        logger.info('Shutting down bot...')
        await service.close()
        await redis.aclose()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Bot stopped by user.')
    except Exception as exception:
        logger.error(f'An unexpected error occurred: {exception}')
