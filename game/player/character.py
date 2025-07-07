import math
import time
from datetime import datetime, timezone
from multiprocessing import Process
from threading import Semaphore, Thread
from typing import Optional, Any, Tuple

from game.player.action import Action
from game.scenario.scenario import Scenario
from utils.request import request


class Character:

    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.action = Action(self)

        self._queue: list[Process] = []
        self._processing_scenario: Process | None = None
        self._queue_lock: Semaphore = Semaphore(0)

        def _schedule():
            while True:
                self._queue_lock.acquire()
                process = self._queue.pop(0)
                process.start()
                self._processing_scenario = process
                process.join()
                self._processing_scenario = None
        Thread(target=_schedule, daemon=True).start()


    def add_queue(self, scenario: Scenario, index: int = -1):
        """
        Set a new scenario to a character.
        :param scenario: type of Scenario
        :param args: args for scenario __init__
        :param index: index to add in queue
        :return:
        """
        self._queue.insert(index, Process(target=scenario.run, daemon=True))
        self._queue_lock.release()

    def cancel(self):
        """
        Stop the actual Scenario to switch to the next
        """
        if self._processing_scenario:
            self._processing_scenario.terminate()

    def stop(self):
        """
        Stop all Scenario in queue
        """
        self._queue.clear()
        self.cancel()

    def wait_cooldown(self):
        """
        Wait a character cooldown with a blocking function
        :return: None
        """
        time.sleep(self.get_cooldown())

    def get_all_data(self) -> Optional[dict[str, Any]]:
        """
        Get all data from the json response API to this character
        :return: Optional[dict[str, Any]]
        """
        return request("GET", f"/characters/{self.name}").json()["data"]

    def get_cooldown(self) -> int:
        """
        Get the actual cooldown of this character
        :return:
        """
        date_str = self.get_all_data()["cooldown_expiration"]
        date_str = date_str.replace("Z", "+00:00")
        date = datetime.fromisoformat(date_str)
        now = datetime.now(timezone.utc)
        return max(math.ceil((date - now).total_seconds()), 0)

    def get_hp(self) -> int:
        """
        Get amount of HP
        :return: int
        """
        return self.get_all_data()["hp"]

    def get_x(self) -> int:
        """
        Get X of your current tile
        :return: int
        """
        return self.get_all_data()["x"]

    def get_y(self) -> Optional[int]:
        """
        Get Y of your current tile
        :return:
        """
        return self.get_all_data()["y"]

    def get_position(self) -> Tuple[int, int]:
        """
        Get X and Y of your current tile
        :return: Tuple[int, int]
        """
        data = self.get_all_data()
        return data["x"], data["y"]

    def get_inventory(self) -> dict[str, int]:
        """
        Get character's inventory
        :return: Dict of item's information in inventory
        """
        return {item["code"]: item["quantity"] for item in self.get_all_data()["inventory"] if item["code"]}

    def get_inventory_max_size(self) -> int:
        """
        Get character's inventory size
        :return: int
        """
        return self.get_all_data()["inventory_max_items"]

    def get_gold(self) -> int:
        """
        Get character's gold
        :return:
        """
        return self.get_all_data()["gold"]

    def _is_full_life(self) -> bool:
        """
        Check if character is full life
        :return: boolean
        """
        data = self.get_all_data()
        return data["hp"] == data["max_hp"]