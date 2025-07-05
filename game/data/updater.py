from abc import ABC, abstractmethod


class Updater(ABC):

    @staticmethod
    @abstractmethod
    def update() -> None:
        """
        Update static file data from API
        :return: None
        """
        pass
