from game.player.character import Character
from utils.macros.do_and_back import do_and_back
from utils.macros.empty_inventory_in_bank import empty_inventory_in_bank


def farm_gathering(character: Character, farm_tile: (int, int)) -> None:
    while True:
        # Make sure the character is on the right tile
        r = character.action.move(*farm_tile)

        if r.status_code == 490:
            break

    # Start gathering
    while True:
        r = character.action.gathering()

        if r.status_code == 497:
            # When inventory is full

            # Empty that in a bank and return farming
            do_and_back(character, empty_inventory_in_bank, character, move=True)
