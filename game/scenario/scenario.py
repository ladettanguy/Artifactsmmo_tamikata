from abc import ABC, abstractmethod


class Scenario(ABC):

    @abstractmethod
    def run(self):
        """
        Run the scenario.
        """
