"""
Модуль содержит базовый класс BaseHandler для обработки команд и сообщений Telegram-бота.

BaseHandler предоставляет абстрактный интерфейс для регистрации хэндлеров,
маршрутизации сообщений и управления командами бота.
"""

from abc import ABC, abstractmethod
from typing import List, Callable, Awaitable, Any, Dict

# Сторонние библиотеки
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, BotCommand

# Локальные импорты
from core.base_service import BaseService
from core.command import Command as Cmd


class BaseHandler(ABC):
    """
    Базовый класс для обработчиков команд и сообщений Telegram-бота.

    Предоставляет методы для регистрации хэндлеров, маршрутизации сообщений
    и управления командами бота.
    """

    def __init__(
        self,
        service: BaseService,
        commands: Dict[str, Cmd]
    ):
        """
        Инициализирует базовый обработчик.

        Args:
            service (BaseService): Сервис для бизнес-логики.
            commands (Dict[str, Cmd]): Словарь команд бота.
        """
        self.__router = Router()
        self._service = service
        self._commands = commands
        self.__bot_commands: List[BotCommand] = []

    @abstractmethod
    def register_handlers(self) -> None:
        """
        Абстрактный метод для регистрации хэндлеров.

        Должен быть реализован в каждом дочернем классе.
        """

    def _register_router(
        self,
        callback: Callable[[Message], Awaitable[Any]],
        cmd_info: Cmd,
        create_command_pallete: bool = True
    ) -> None:
        """
        Регистрирует хэндлер для команды и добавляет команду в меню бота.

        Args:
            callback (Callable): Функция-обработчик сообщения.
            cmd_info (Cmd): Информация о команде.
            create_command_pallete (bool): Флаг для создания команды в меню бота.
        """
        # Регистрация хэндлера для команды
        @self.__router.message(Command(cmd_info.name))
        async def command_handler(message: Message):
            await callback(message)

        if create_command_pallete:
            # Добавляем объект BotCommand для настройки меню команд
            self.__bot_commands.append(
                BotCommand(command=cmd_info.name, description=cmd_info.description)
            )

    def _find_method(self, name: str) -> callable:
        """
        Находит метод по имени в текущем объекте.

        Args:
            name (str): Имя метода.

        Returns:
            callable: Метод, если он существует и вызываемый, иначе None.
        """
        method = getattr(self, name, None)  # Используем getattr для получения атрибута
        return method if callable(method) else None  # Проверяем, является ли объект вызываемым

    @property
    def router(self) -> Router:
        """
        Возвращает роутер для маршрутизации сообщений.

        Returns:
            Router: Роутер aiogram.
        """
        return self.__router

    @property
    def bot_commands(self) -> List[BotCommand]:
        """
        Возвращает список команд бота для настройки меню.

        Returns:
            List[BotCommand]: Список команд бота.
        """
        return self.__bot_commands
