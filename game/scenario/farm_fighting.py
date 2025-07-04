from game.player.character import Character
from game.scenario.scenario import Scenario
from utils.macros.do_and_back import do_and_back
from utils.macros.empty_inventory_in_bank import empty_inventory_in_bank


class FarmeFighting(Scenario):

    def __init__(self, character: Character, farm_tile: (int, int)) -> None:
        self.character = character
        self.farm_tile = farm_tile

    def pre_loop(self):
        self.character.wait_cooldown()
        self.character.action.move(*self.farm_tile)


    def loop(self):
        r = self.character.action.fight()

        if r.status_code == 497:
            # When inventory is full

            # Empty that in a bank and return farming
            do_and_back(self.character, empty_inventory_in_bank, self.character, move=True)

        self.character.action.rest()

    def post_loop(self):
        self.character.action.rest()
