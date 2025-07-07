from requests import Response

from game.bank import Bank


def empty_inventory_in_bank(character: "Character", move: bool = False) -> Response:
    """
    Empty the inventory in the bank
    :param character: Character to empty
    :param move: optional param to automatically move in bank tile
    :return: requests.Response
    """
    if move:
        character.action.move(*Bank.get_nearest_bank(character.get_position()))
    return character.action.bank_deposit_items(character.get_inventory())
