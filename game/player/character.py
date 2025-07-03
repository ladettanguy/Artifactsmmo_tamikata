import time

from typing import Optional, Any, Tuple

from game.player.action import Action
from utils.request import request


class Character:

    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.action = Action(self.name)

    def wait_cooldown(self):
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
        return self.get_all_data()["cooldown"]

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

    def get_inventory(self) -> list[dict[str, str|int]]:
        """
        Get character's inventory
        :return: List of item's information in inventory
        """
        return self.get_all_data()["inventory"]
