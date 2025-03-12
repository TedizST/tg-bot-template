"""
Модуль содержит обработчик CommonHandler для обработки общих команд Telegram-бота.

CommonHandler реализует регистрацию хэндлеров для команд, таких как /start и /help,
и делегирует их выполнение соответствующим методам сервиса.
"""

from aiogram.types import Message

from core.base_handler import BaseHandler


class CommonHandler(BaseHandler):
    """
    Обработчик общих команд Telegram-бота.

    Регистрирует хэндлеры для команд, таких как /start и /help, и делегирует их
    выполнение методам сервиса.
    """

    def register_handlers(self):
        """
        Регистрирует хэндлеры для всех команд из словаря команд.

        Для каждой команды вызывается метод _register_router, который связывает
        команду с соответствующим обработчиком.
        """
        for _, value in self._commands.items():
            self._register_router(
                callback=self._find_method(value.name),
                cmd_info=value,
                create_command_pallete=False
            )

    async def start(self, message: Message):
        """
        Обрабатывает команду /start.

        Args:
            message (Message): Входящее сообщение от пользователя.
        """
        await self._service.start(message)

    async def help(self, message: Message):
        """
        Обрабатывает команду /help.

        Args:
            message (Message): Входящее сообщение от пользователя.
        """
        await self._service.help(message)
