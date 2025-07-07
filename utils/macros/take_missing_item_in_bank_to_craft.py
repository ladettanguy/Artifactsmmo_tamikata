import math
from typing import Optional

import requests

from game.items import Items
from game.maps import Maps
from game.player.character import Character


def take_missing_item_in_bank_to_craft(character: Character, item_code: str, quantity: int) ->  Optional[requests.Response]:
    """
    Move to the bank, and take missing item for a craft.
    :param character: Character object
    :param item_code: str, item code
    :param quantity: int, quantity to craft
    :return: Optional[requests.Response]
    """
    if not Items.is_craftable(item_code):
        return None

    map_tile = Maps.POINT_OF_INTEREST.bank.bank
    character.action.move(*map_tile)

    item_info = Items.get(item_code)
    inventory = character.get_inventory()
    craft = item_info["craft"]
    nb_craft = math.ceil(quantity / craft["quantity"])
    items_needed = {item["code"]: max(0, item["quantity"] * nb_craft - inventory.get(item["code"], 0))
                    for item in craft["items"]}

    r = character.action.bank_withdraw_items(items_needed)
    return r