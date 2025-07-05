from game.data.items_loader import ItemsLoader
from game.game import Game
from game.npcs import NPCs
from game.scenario.farm_gathering import FarmGathering
from game.scenario.farm_fighting import FarmFighting
from game.maps import Maps
from game.items import Items

game = Game()

#for character_name, character_object in game.get_characters().items():
#    game.set_scenario(character_name, FarmFighting, args=(character_object, Maps.POINT_OF_INTEREST.monster.chicken))

#game.start()
print(Maps.POINT_OF_INTEREST.bank.bank)
print(Items.get("wooden_staff"))
