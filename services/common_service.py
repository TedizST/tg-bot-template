"""
Модуль содержит сервис CommonService для обработки команд Telegram-бота.

CommonService реализует методы для выполнения команд, таких как /start и /help,
и отправляет соответствующие ответы пользователям.
"""

from aiogram.types import Message

from core.base_service import BaseService


class CommonService(BaseService):
    """
    Сервис для обработки общих команд Telegram-бота.

    Реализует методы для выполнения команд, таких как /start и /help,
    и отправляет соответствующие ответы пользователям.
    """

    async def start(self, message: Message):
        """
        Обрабатывает команду /start.

        Отправляет приветственное сообщение пользователю.

        Args:
            message (Message): Входящее сообщение от пользователя.
        """
        await message.answer("Это стартовая команда.")

    async def help(self, message: Message):
        """
        Обрабатывает команду /help.

        Отправляет справочное сообщение пользователю.

        Args:
            message (Message): Входящее сообщение от пользователя.
        """
        await message.answer("Это справка по боту.")
