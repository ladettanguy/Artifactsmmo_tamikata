import math

import requests

from game.bank import Bank
from game.maps import Maps
from utils.macros.empty_inventory_in_bank import empty_inventory_in_bank


def complete_items_task(character: "Character") -> requests.Response:
    """
    Secure complete task. Go take items in bank, and make forth and back to complete current task
    :param character: Character object
    :return: requests.Response
    """
    task_info = character.get_task_info()
    empty_inventory_in_bank(character, move=True)
    quantity = task_info["task_total"] - task_info["task_progress"]
    inv_size = character.get_inventory_max_size()
    trade_master_tile = Maps.POINT_OF_INTEREST.tasks_master["items"]
    bank_tile = Bank.get_nearest_bank(Maps.POINT_OF_INTEREST.tasks_master["items"])
    while quantity > 0:
        trade_quantity = min(quantity, inv_size)
        character.action.move(*bank_tile)
        character.action.bank_withdraw_items({task_info["task"]: trade_quantity})
        character.action.move(*trade_master_tile)
        character.action.task_master_trade(task_info["task"], trade_quantity)
        quantity -= trade_quantity
    return character.action.task_complete()