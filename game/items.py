import math
from typing import Any

from game.data.items_loader import ItemsLoader


class Items:

    _items = ItemsLoader.load()

    @classmethod
    def get_item_need_to_craft(cls, item_code, quantity):
        """

        :param item_code:
        :param quantity:
        :return:
        """
        item_info = Items.get(item_code)
        if "craft" not in item_info:
            return None

        craft = item_info["craft"]
        nb_craft = math.ceil(quantity / craft["quantity"])
        return {item["code"]: item["quantity"] * nb_craft for item in craft["items"]}

    @classmethod
    def is_craftable(cls, item_code: str) -> bool:
        """
        Check if an item is craftable
        :param item_code: Item code
        :return: boolean
        """
        item = cls.get(item_code)
        return item is not None and "craft" in item

    @classmethod
    def get(cls, item_code: str) -> dict[str, Any]:
        """
        Get item information
        :param item_code: Item code
        :return: dict[str, Any], like:
        {
            "level": 1,
            "type": "consumable",
            "subtype": "food",
            "description": "description text ipsum",
            "conditions": [],
            "effects": [
                {
                    "code": "heal",
                    "value": 75,
                    "description": "Heal 75 HP when the item is used."
                }
            ],
            "craft": {
                "skill": "cooking",
                "level": 1,
                "items": [
                    {
                        "code": "gudgeon",
                        "quantity": 1
                    }
                ],
                "quantity": 1
            },
            "tradeable": true
        }
        """
        return cls._items[item_code]
