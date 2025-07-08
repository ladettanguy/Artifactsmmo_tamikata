from game.game import Game
from game.scenario.craft import Craft
from game.scenario.farm_fighting import FarmFighting
from game.maps import Maps
from game.scenario.farm_gathering import FarmGathering

game = Game()

characters = game.characters
t1 = characters["tamikata1"]
t2 = characters["tamikata2"]
t3 = characters["tamikata3"]
t4 = characters["tamikata4"]
t5 = characters["tamikata5"]

t1.add_queue(FarmFighting(t1, Maps.POINT_OF_INTEREST.monster.sheep))
t2.add_queue(FarmGathering(t2, Maps.POINT_OF_INTEREST.resource.coal_rocks))
t3.add_queue(FarmGathering(t3, Maps.POINT_OF_INTEREST.resource.birch_tree))
t4.add_queue(FarmGathering(t4, Maps.POINT_OF_INTEREST.resource.trout_fishing_spot))
t5.add_queue(FarmGathering(t5, Maps.POINT_OF_INTEREST.resource.glowstem))

game.start()
