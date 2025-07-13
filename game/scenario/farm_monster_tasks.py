from game.items import Items
from game.maps import Maps
from game.player.character import Character
from game.resources import Resources
from game.scenario.craft import Craft
from game.scenario.farm_fighting import FarmFighting
from game.scenario.farm_gathering import FarmGathering
from game.scenario.scenario import Scenario
from utils.macros.complete_items_task import complete_items_task
from utils.macros.take_task import take_task


class FarmMonsterTasks(Scenario):

    def __init__(self, character: Character, nb_loop: int = -1):
        self.character = character
        self.nb_loop = nb_loop

    def run(self):
        def response_to_task_info(r):
            data = r.json()["data"]["character"]
            return {"task": data["task"], "task_type": data["task_type"], "task_progress": 0, "task_total": data["task_total"]}

        actual_task = self.character.get_task_info()
        if not actual_task["task"]:
            actual_task = response_to_task_info(take_task(self.character, "monsters"))

        if actual_task["task_type"] != "monsters":
            return

        i = 0
        while i != self.nb_loop:
            monster = actual_task["task"]
            monsters_quantity = actual_task["task_total"] - actual_task["task_progress"]
            map_tile = Maps.POINT_OF_INTEREST.monsters[monster]
            alive = FarmFighting(self.character, map_tile, nb_loop=monsters_quantity, kaizen=False).run()
            if not alive:
                return
            self.character.action.move(*Maps.POINT_OF_INTEREST.tasks_master[monster])
            self.character.action.task_complete()
            self.character.action.task_new()
            actual_task = response_to_task_info(take_task(self.character, "items"))
            i += 1
