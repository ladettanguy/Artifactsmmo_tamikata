from game.player.character import Character
from game.scenario.scenario import Scenario
from utils.macros.do_and_back import do_and_back
from utils.macros.empty_inventory_in_bank import empty_inventory_in_bank


class FarmGathering(Scenario):

    def __init__(self, character: Character, farm_tile: (int, int), nb_loop: int = -1):
        """
        :param character: Character object
        :param farm_tile: Tuple[int, int]
        :param nb_loop: Number of loops (use it if you don't want a infinite loop) (-1 is infinite)
        """
        self.character = character
        self.farm_tile = farm_tile
        self.nb_loop = nb_loop

    def run(self):
        self.character.wait_cooldown()
        self.character.action.move(*self.farm_tile)

        r = self.character.action.gathering()

        i = 0
        while i != self.nb_loop:
            if r.status_code == 497:
                # When inventory is full

                # Empty that in a bank and return farming
                do_and_back(self.character, empty_inventory_in_bank, self.character, move=True)
            i += 1