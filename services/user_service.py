from aiogram.types import Message

from core.base_service import BaseService

class UserService(BaseService):
    async def start(self, message: Message):
        await message.answer("Это стартовая команда.")

    async def help(self, message: Message):
        await message.answer("Это справка по боту.")