"""
Модуль содержит middleware LoggingMiddleware для логирования событий.

LoggingMiddleware используется для вывода информации о входящих сообщениях,
включая текст сообщения и ID пользователя, отправившего его.
"""

from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware):
    """
    Middleware для логирования входящих сообщений.

    При обработке каждого события выводится информация о тексте сообщения
    и ID пользователя, отправившего его. После логирования управление передается
    следующему обработчику в цепочке.
    """

    async def __call__(self, handler, event: Message, data):
        """
        Обрабатывает входящее событие.

        Логирует текст сообщения и ID пользователя, затем передает управление
        следующему обработчику.

        Args:
            handler: Следующий обработчик в цепочке.
            event (Message): Входящее сообщение.
            data: Дополнительные данные, передаваемые по цепочке middleware.

        Returns:
            Результат выполнения следующего обработчика.
        """
        print(f"[LOG] Обработка события: {event.text} от пользователя {event.from_user.id}")
        return await handler(event, data)
