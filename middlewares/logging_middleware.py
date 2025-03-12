from aiogram import BaseMiddleware
from aiogram.types import Message

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        print(f"[LOG] Обработка события: {event.text} от пользователя {event.from_user.id}")
        return await handler(event, data)