import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers.user_handler import UserHandler
from middlewares.logging_middleware import LoggingMiddleware
from configs import BOT_TOKEN, LOG_LEVEL

async def main():
    # Настройка логирования
    logging.basicConfig(level=getattr(logging, LOG_LEVEL))
    logger = logging.getLogger(__name__)

    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Списко команд в меню бота
    bot_commands = list()

    # Создание экземпляров хэндлеров
    user_handler = UserHandler()

    # Регистрация хэндлеров
    bot_commands.extend(user_handler.register_handlers())

    # Регистрация команд в меню бота
    await bot.set_my_commands(bot_commands)

    # Подключение middleware
    dp.message.middleware(LoggingMiddleware())

    # Подключение роутеров к диспетчеру
    dp.include_router(user_handler.router)

    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())