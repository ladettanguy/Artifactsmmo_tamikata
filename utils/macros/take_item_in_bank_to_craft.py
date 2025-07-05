import math
from typing import Optional

import requests

from game.items import Items
from game.maps import Maps
from game.player.character import Character


def take_missing_item_in_bank_to_craft(character: Character, item_code: str, quantity: int) ->  Optional[requests.Response]:
    map_tile = Maps.POINT_OF_INTEREST.bank.bank
    character.action.move(*map_tile)

    item_info = Items.get(item_code)
    if "craft" not in item_info:
        return None

    inventory = character.get_inventory()
    craft = item_info["craft"]
    nb_craft = math.ceil(quantity / craft["quantity"])
    items_needed = {item["code"]: max(0, item["quantity"] * nb_craft - inventory.get(item["code"], 0))
                    for item in craft["items"]}

    r = character.action.bank_withdraw_items(items_needed)
    return r