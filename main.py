from game.game import Game
from game.maps import Maps
from game.scenario.craft import Craft
from game.scenario.farm_fighting import FarmFighting
from game.scenario.farm_gathering import FarmGathering
from game.scenario.farm_items_tasks import FarmItemsTasks
from utils.macros.complete_items_task import complete_items_task

game = Game()

characters = game.characters
t1 = characters["tamikata1"]
t2 = characters["tamikata2"]
t3 = characters["tamikata3"]
t4 = characters["tamikata4"]
t5 = characters["tamikata5"]

#t1.add_queue(FarmGathering(t1, Maps.POINT_OF_INTEREST.resource.coal_rocks))
t1.add_queue(FarmFighting(t1, Maps.POINT_OF_INTEREST.monster.cow))
#t2.add_queue(FarmGathering(t2, Maps.POINT_OF_INTEREST.resource.gold_rocks))
t2.add_queue(FarmFighting(t2, Maps.POINT_OF_INTEREST.monster.chicken))
#t3.add_queue(FarmGathering(t3, Maps.POINT_OF_INTEREST.resource.dead_tree))
t3.add_queue(FarmFighting(t3, Maps.POINT_OF_INTEREST.monster.chicken))
#t4.add_queue(FarmGathering(t4, Maps.POINT_OF_INTEREST.resource.bass_fishing_spot))
t4.add_queue(FarmFighting(t4, Maps.POINT_OF_INTEREST.monster.chicken))
t5.add_queue(FarmItemsTasks(t5))

game.start()
