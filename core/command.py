"""
Модуль содержит класс Command для представления команд Telegram-бота.

Класс Command используется для хранения имени и описания команды.
Он предоставляет свойства для доступа к этим данным.
"""

from abc import ABC


class Command(ABC):
    """
    Класс Command представляет команду Telegram-бота.

    Содержит имя и описание команды, которые используются для регистрации
    команд в боте и отображения их в меню.
    """

    def __init__(self, name: str, description: str):
        """
        Инициализирует объект команды.

        Args:
            name (str): Имя команды (например, "start").
            description (str): Описание команды (например, "Начать работу с ботом").
        """
        self.__name = name
        self.__description = description

    @property
    def name(self) -> str:
        """
        Возвращает имя команды.

        Returns:
            str: Имя команды.
        """
        return self.__name

    @property
    def description(self) -> str:
        """
        Возвращает описание команды.

        Returns:
            str: Описание команды.
        """
        return self.__description
