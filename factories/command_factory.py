from typing import Callable, Awaitable, Any
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from core.cmd_info import CmdInfo

class CommandFactory:
    @staticmethod
    def register(
        router: Router,
        callback: Callable[[Message], Awaitable[Any]],
        cmd_info: CmdInfo,
        create_command_pallete=True
    ) -> BotCommand | None:
        """
        Регистрирует команду в роутере и возвращает объект BotCommand.

        :param router: Экземпляр Router для регистрации хэндлера.
        :param command_name: Имя команды (например, "start").
        :param callback: Асинхронная функция-обработчик команды.
        :param description: Описание команды для меню команд Telegram.
        :return: Объект BotCommand.
        """
        # Регистрация хэндлера для команды
        @router.message(Command(cmd_info.name))
        async def command_handler(message: Message):
            await callback(message)

        if create_command_pallete:
            # Возвращаем объект BotCommand для настройки меню команд
            return BotCommand(command=cmd_info.name, description=cmd_info.description)
        else:
            return None