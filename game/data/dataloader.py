from abc import ABC, abstractmethod
from typing import Any


class DataLoader(ABC):

    @staticmethod
    @abstractmethod
    def load() -> dict[str, Any]:
        """
        Load data in a python dictionary format
        :return: Dict[str, Any]
        """
        pass