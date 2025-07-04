from abc import ABC, abstractmethod


class DataLoader(ABC):

    @staticmethod
    @abstractmethod
    def load():
        pass