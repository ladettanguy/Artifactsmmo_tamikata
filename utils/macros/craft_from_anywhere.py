import requests
from typing import Optional

from game.items import Items
from game.maps import Maps
from game.player.character import Character


def craft_from_anywhere(character: Character, item_code: str, quantity: int) -> Optional[requests.Response]:
    """
    Craft an item without knowing where crafting it
    :param character: Character object
    :param item_code: Item code
    :param quantity:
    :return:
    """

    if not Items.is_craftable(item_code):
        return None

    item_info: dict = Items.get(item_code)

    skill_code = item_info["craft"]["skill"]
    map_tile = Maps.POINT_OF_INTEREST.workshop[skill_code]

    character.action.move(*map_tile)
    r = character.action.crafting(item_code, quantity)
    return r
