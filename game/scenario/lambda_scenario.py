from typing import Callable, Any

from game.scenario.scenario import Scenario


class LambdaScenario(Scenario):

    def __init__(self, target: Callable, args: tuple[Any] = ()):
        self._run = target
        self.args = args

    def run(self):
        self._run(*self.args)
