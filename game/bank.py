from typing import Any

from game.maps import Maps
from utils.request import request_all_pages, request


class Bank:

    _banks = [(int(coord.split(" ")[0]), int(coord.split(" ")[1]))
              for coord, map in Maps.get_all_map().items() if map["content"] and map["content"]["type"] == "bank"]

    @classmethod
    def get_nearest_bank(cls, actual_tile: tuple[int, int]) -> tuple[int, int]:
        """
        Get the nearest bank coord x, y
        :param actual_tile: tuple[int, int], Your actual x, y
        :return: tuple[int, int], bank coord
        """
        x, y = actual_tile

        def distance2(p):
            return (p[0] - x) ** 2 + (p[1] - y) ** 2

        return min(cls._banks, key=distance2)

    @staticmethod
    def get_bank_item_info() -> list[dict[str, Any]]:
        """
        Fetch all items in your bank.
        :return: list of items bank storage, like:
            [{"code": "string", "quantity": 1}, ...]
        """
        return request_all_pages("GET", "/my/bank/items")

    @staticmethod
    def get_bank_info() -> dict[str, int]:
        """
        Fetch bank details.
        :return: dict[str, int] like: {"slots": 0, "expansions": 0, "next_expansion_cost": 0, "gold": 0}
        """
        return request("GET", "/my/bank").json()["data"]
