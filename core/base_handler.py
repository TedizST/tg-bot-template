from abc import ABC, abstractmethod
from aiogram import Router
from aiogram.types import BotCommand

from typing import List

class BaseHandler(ABC):
    def __init__(self):
        self.__router = Router()

    @abstractmethod
    def register_handlers(self) -> List[BotCommand]:
        """
        Абстрактный метод для регистрации хэндлеров.
        Должен быть реализован в каждом дочернем классе.
        """
        pass

    @property
    def router(self) -> Router:
        """
        Метод для получения роутера.
        """
        return self.__router