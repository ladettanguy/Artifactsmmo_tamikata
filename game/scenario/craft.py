import math

from game.items import Items
from game.player.character import Character
from game.scenario.scenario import Scenario
from utils.macros.craft_from_anywhere import craft_from_anywhere
from utils.macros.empty_inventory_in_bank import empty_inventory_in_bank
from utils.macros.take_missing_item_in_bank_to_craft import take_missing_item_in_bank_to_craft


class Craft(Scenario):

    def __init__(self, character: Character, item_code: str, quantity: int):
        self.character = character
        self.item_code = item_code
        self.quantity = quantity


    def run(self):
        inventory_size = self.character.get_inventory_max_size()
        items_needed = Items.get_item_need_to_craft(self.item_code, self.quantity)
        if not items_needed:
            return

        total_quantity = sum(list(items_needed.values()))
        quantity_remaining = self.quantity
        nb_repetition = math.ceil(total_quantity / inventory_size)
        quantity_by_repetition = math.floor(quantity_remaining / nb_repetition)
        for _ in range(nb_repetition):
            empty_inventory_in_bank(self.character, move=True)
            take_missing_item_in_bank_to_craft(self.character, self.item_code, min(quantity_by_repetition, quantity_remaining))
            craft_from_anywhere(self.character, self.item_code, min(quantity_by_repetition, quantity_remaining))
            quantity_remaining -= quantity_by_repetition
        empty_inventory_in_bank(self.character, move=True)