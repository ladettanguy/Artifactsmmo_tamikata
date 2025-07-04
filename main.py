from game.game import Game
from game.scenario.farm_gathering import FarmGathering

game = Game()

for character_name, character_object in game.get_characters().items():
    game.set_scenario(character_name, FarmGathering, args=(character_object, (5, 2)))

game.start()
