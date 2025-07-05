from abc import ABC, abstractmethod


class Scenario(ABC):

    def __init__(self, *args, nb_loop=0):
        self.cancel_loop = False
        self.nb_loop = nb_loop
        self.nb_iter = 0

    @abstractmethod
    def pre_loop(self):
        """
        This method is a setup method for your scenario. This will call at first before the loop and once time.
        :return: None
        """
        pass

    @abstractmethod
    def loop(self):
        """
        This is the loop method. It's going to call several time until called self.nb_loop times or canceled by cancel().
        :return: None
        """
        pass

    @abstractmethod
    def post_loop(self):
        """
        This the post loop method. It's going to call once, after loop execution.
        """
        pass

    def run(self):
        """
        Run the scenario.
        """
        self.pre_loop()
        while not self.cancel_loop:
            self.loop()
            self.nb_iter += 1
            if self.nb_iter == self.nb_loop:
                break
        self.post_loop()

    def cancel(self):
        """
        Cancel this scenario. Used for a ThreadScenario to cancel.
        """
        self.cancel_loop = True
