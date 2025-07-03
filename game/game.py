from typing import Any

from utils.request import request
from game.player.character import Character


def create_character(name: str, skin: str) -> Character:
    r = request("POST", "characters/create", data={"name": name, "skin": skin})
    if r.status_code != 200:
        return

    return Character(r.json()["data"])

def get_characters() -> dict[str, Character]:
    """
    use to have a spécific character from his name
    :param name: character's name
    :return: Character or None
    """
    return {d["name"]: Character(data=d) for d in request("GET", "/my/characters").json()["data"]}

def get_bank_item_info() -> dict[str, Any]:
    """
    Get items bank storage
    :return: Dictionary of items bank storage
    """
    return request("GET", "/my/bank/items").json()["data"]