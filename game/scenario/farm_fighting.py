from game.player.character import Character
from game.scenario.scenario import Scenario
from utils.macros.do_and_back import do_and_back
from utils.macros.empty_inventory_in_bank import empty_inventory_in_bank


class FarmFighting(Scenario):

    def __init__(self, character: Character, farm_tile: (int, int), nb_loop: int = -1, kaizen: bool = True):
        """
        :param character: Character object
        :param farm_tile: tuple[int, int]
        :param nb_loop: Number of loops (use it if you don't want a infinite loop) (-1 is infinite)
        :param kaizen: bool, kaïzen mod. it's retry fight if character die
        """
        self.character = character
        self.farm_tile = farm_tile
        self.nb_loop = nb_loop
        self.kaizen = kaizen

    def run(self):
        self.character.action.move(*self.farm_tile)
        self.character.action.rest()

        i = 0
        while i != self.nb_loop:
            r = self.character.action.fight()

            if r.status_code == 200:
                info_battle = r.json()["data"]
                if info_battle["fight"]["result"] != "win":
                    if self.kaizen:
                        self.character.action.move(*self.farm_tile)
                        self.character.action.rest()
                    else:
                        return False

            if r.status_code == 497:
                # When inventory is full

                # Empty that in a bank and return farming
                do_and_back(self.character, empty_inventory_in_bank, self.character, move=True)

            self.character.action.rest()
            i += 1
        return True
