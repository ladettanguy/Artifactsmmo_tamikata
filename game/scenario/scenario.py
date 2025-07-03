from abc import ABC, abstractmethod


class Scenario(ABC):

    def __init__(self, *args):
        self.cancel_loop = False

    @abstractmethod
    def pre_loop(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    @abstractmethod
    def post_loop(self):
        pass

    def run(self):
        self.pre_loop()
        while not self.cancel_loop:
            self.loop()
        self.post_loop()

    def cancel(self):
        self.cancel_loop = True