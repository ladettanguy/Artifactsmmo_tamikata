from requests import Response


def empty_inventory_in_bank(character: "Character", move: bool = False) -> Response:
    """
    Empty the inventory in the bank
    :param character: Character to empty
    :param move: optional param to automatically move in bank tile
    :return: requests.Response
    """
    if move:
        character.action.move(4, 1)
    return character.action.bank_deposit_item(character.get_inventory())
