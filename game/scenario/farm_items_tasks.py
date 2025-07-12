from game.items import Items
from game.player.character import Character
from game.resources import Resources
from game.scenario.craft import Craft
from game.scenario.farm_gathering import FarmGathering
from game.scenario.scenario import Scenario
from utils.macros.complete_items_task import complete_items_task
from utils.macros.take_task import take_task


class FarmItemsTasks(Scenario):

    def __init__(self, character: Character, nb_loop: int = -1):
        self.character = character
        self.nb_loop = nb_loop

    def run(self):
        def response_to_task_info(r):
            data = r.json()["data"]["character"]
            return {"task": data["task"], "task_type": data["task_type"], "task_progress": 0, "task_total": data["task_total"]}

        actual_task = self.character.get_task_info()
        if not actual_task["task"]:
            actual_task = response_to_task_info(take_task(self.character, "items"))

        if actual_task["task_type"] != "items":
            return

        i = 0
        while i != self.nb_loop:
            item = actual_task["task"]
            item_quantity = actual_task["task_total"] - actual_task["task_progress"]
            try:
                map_tile = Resources.get_map_resource(item)
                if not map_tile:
                    raise KeyError
                FarmGathering(self.character, map_tile, nb_loop=item_quantity).run()
            except KeyError:
                item_for_task = Items.get_item_need_to_craft(item, item_quantity)
                for item_code, quantity in item_for_task.items():
                    map_tile = Resources.get_map_resource(item_code)
                    FarmGathering(self.character, map_tile, nb_loop=quantity).run()
                Craft(self.character, actual_task["task"], actual_task["task_total"]).run()
            complete_items_task(self.character)
            actual_task = response_to_task_info(take_task(self.character, "items"))
            i += 1
