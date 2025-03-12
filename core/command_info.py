from abc import ABC

class CommandInfo(ABC):
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    