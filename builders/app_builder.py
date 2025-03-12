"""
Модуль для запуска Telegram-бота.

Содержит класс AppBuilder, который отвечает за инициализацию и запуск бота.
"""

import logging

from aiogram import Bot, Dispatcher

from configs import BOT_TOKEN, LOG_LEVEL
from handlers.common_handler import CommonHandler
from services.common_service import CommonService
from commands import user_commands
from middlewares.logging_middleware import LoggingMiddleware


class AppBuilder:
    """
    Класс AppBuilder отвечает за инициализацию и запуск Telegram-бота.

    Он выполняет настройку логгирования, бота, диспетчера, обработчиков,
    команд меню и промежуточного ПО (middlewares). После завершения настройки
    запускает бота в режиме polling.
    """

    def __init__(self):
        """
        Конструктор класса AppBuilder.

        Инициализирует все необходимые компоненты для работы бота:
        - Логгер
        - Экземпляр бота
        - Диспетчер
        - Обработчики
        - Команды меню
        - Промежуточное ПО
        """
        self.__handlers = []
        self.__bot_commands = []
        self.__init_logger()
        self.__init_bot()
        self.__init_dp()
        self.__init_handlers()
        self.__register_handlers()
        self.__register_middlewares()

    def __init_logger(self):
        """
        Инициализирует систему логгирования.

        Настройка уровня логгирования происходит на основе значения LOG_LEVEL
        из конфигурационного файла.
        """
        logging.basicConfig(level=getattr(logging, LOG_LEVEL))
        self.__logger = logging.getLogger(__name__)

    def __init_bot(self):
        """
        Инициализирует экземпляр Telegram-бота.

        Создает объект Bot с использованием токена из конфигурационного файла.
        """
        self.__bot = Bot(token=BOT_TOKEN)

    def __init_dp(self):
        """
        Инициализирует диспетчер для обработки событий.

        Создает экземпляр Dispatcher, который будет управлять маршрутизацией
        входящих сообщений и вызовов.
        """
        self.__dp = Dispatcher()

    def __init_handlers(self):
        """
        Инициализирует обработчики.

        Создает экземпляры обработчиков (например, CommonHandler) и добавляет
        их в список для последующей регистрации.
        """
        common_handler = CommonHandler(service=CommonService(), commands=user_commands.commands)
        self.__handlers.append(common_handler)

    def __register_handlers(self):
        """
        Регистрирует обработчики и связанные с ними команды.

        Для каждого обработчика регистрируются маршруты (routers),
        а также добавляются команды меню в список для последующей настройки.
        """
        for handler in self.__handlers:
            handler.register_handlers()
            self.__bot_commands.extend(handler.bot_commands)
            self.__dp.include_router(handler.router)

    async def put_menu(self):
        """
        Регистрирует команды меню для бота.

        Если список команд меню не пустой, они устанавливаются для бота
        через метод set_my_commands.
        """
        if len(self.__bot_commands) != 0:
            await self.__bot.delete_my_commands()
            await self.__bot.set_my_commands(self.__bot_commands)

    def __register_middlewares(self):
        """
        Регистрирует промежуточное ПО (middlewares).

        Добавляет middleware для обработки сообщений, например,
        LoggingMiddleware, которое обеспечивает логирование событий.
        """
        self.__dp.message.middleware(LoggingMiddleware())

    async def start(self):
        """
        Запускает бота в режиме polling.

        Начинает процесс обработки входящих сообщений и вызовов.
        """
        self.__logger.info("Запуск бота...")
        await self.__dp.start_polling(self.__bot)

    @staticmethod
    async def build() -> 'AppBuilder':
        """
        Создает и настраивает экземпляр AppBuilder.

        Метод выполняет следующие действия:
        1. Создает новый экземпляр класса AppBuilder.
        2. Вызывает метод для настройки меню команд бота.
        3. Возвращает готовый экземпляр AppBuilder для дальнейшего использования.

        Returns:
            AppBuilder: Настроенный экземпляр AppBuilder.
        """
        app = AppBuilder()
        await app.put_menu()  # Используем защищенный метод вместо приватного

        return app
