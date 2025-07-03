from threading import Thread

from game.scenario.scenario import Scenario


class ThreadScenario(Thread):

    def __init__(self, scenario: type[Scenario], name, args=()):
        self.scenario = scenario(*args)
        Thread.__init__(self, target=self.scenario.run, name=name, daemon=True)

    def cancel(self):
        self.scenario.cancel()
        self.join()
