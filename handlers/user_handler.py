from aiogram.types import Message

from core.base_handler import BaseHandler
from commands_infos import user_commands_infos
from factories.command_factory import CommandFactory
from services.user_service import UserService


class UserHandler(BaseHandler):
    def __init__(self, userService: UserService):
        super().__init__()
        self.__userService = userService

    def register_handlers(self):
        bot_commands = [       
            CommandFactory.register(
                 router=self.router, 
                 callback=self.start_command, 
                 cmd_info=user_commands_infos.start,
                ),  
            CommandFactory.register(
                 router=self.router,
                 callback=self.help_command, 
                 cmd_info=user_commands_infos.help,
            )
        ]

        return filter(lambda bt_cmd: bt_cmd is not None, bot_commands)
    
    async def start_command(self, message: Message):
        await self.__userService.start(message)

    async def help_command(self, message: Message):
        await self.__userService.help(message)