from aiogram.types import Message
from core.base_handler import BaseHandler
from cmds_infos import user_cmds_infos

from factories.command_factory import CommandFactory

class UserHandler(BaseHandler):
    def register_handlers(self):
        bot_commands = [       
            CommandFactory.register(
                 router=self.router, 
                 callback=UserHandler.start_command, 
                 cmd_info=user_cmds_infos.start,
                ),  
            CommandFactory.register(
                 router=self.router,
                 callback=UserHandler.start_command, 
                 cmd_info=user_cmds_infos.help,
            )
        ]

        return filter(lambda bt_cmd: bt_cmd is not None, bot_commands)
    
    @staticmethod
    async def start_command(message: Message):
        await message.answer("Это стартовая команда.")

    @staticmethod
    async def help_command(message: Message):
            await message.answer("Это справка по боту.")