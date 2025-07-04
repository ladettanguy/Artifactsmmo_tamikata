from abc import ABC, abstractmethod


class Updater(ABC):

    @staticmethod
    @abstractmethod
    def update():
        pass
