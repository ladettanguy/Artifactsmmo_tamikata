from typing import Any, Optional

from requests import Response
from utils.request import request
from utils.decorator import waitable

class Action:

    def __init__(self, character: "Character"):
        self.name = character.name
        self.character = character

    @waitable
    def move(self, x: int, y: int) -> Optional[Response]:
        """
        Moves a character on the map using the map's X and Y position.
        :param x: X Coordinate of wanted tile
        :param y: Y Coordinate of wanted tile
        :return: requests.Response
        """
        if not self.character.get_position() == (x, y):
            return request("POST",
                            f"my/{self.name}/action/move",
                            data={"x": x, "y": y})
        return None

    @waitable
    def fight(self) -> Response:
        """
        Start a fight against a monster on the character's map.
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/fight")

    @waitable
    def rest(self) -> Response:
        """
        Recovers hit points by resting. (1 second per 5 HP, minimum 3 seconds)
        :return: requests.Response
        """
        if not self.character._is_full_life():
            return request("POST",
                           f"my/{self.name}/action/rest")

    @waitable
    def gathering(self) -> Response:
        """
        Harvest a resource on the character's map.
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/gathering")

    @waitable
    def recycling(self, code: str, quantity: int) -> Response:
        """
        Recycling an item. The character must be on a map with a workshop (only for equipments and weapons).
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/recycling",
                       data={"code": code, "quantity": quantity})

    @waitable
    def use(self, code: str, quantity: int) -> Response:
        """
        Use an item as a consumable.
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/use",
                       data={"code": code, "quantity": quantity})

    @waitable
    def equip(self, code: str, slot: str, quantity: int) -> Response:
        """
        Equip an item on your character.
        :param code: item code name
        :param slot: slot name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/equip",
                       data={"code": code, "slot": slot, "quantity": quantity})

    @waitable
    def unequip(self, slot: str, quantity: int) -> Response:
        """
        Unequip an item on your character.
        :param slot: slot name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/unequip",
                       data={"slot": slot, "quantity": quantity})

    @waitable
    def crafting(self, code: str, quantity: int) -> Response:
        """
        Crafting an item. The character must be on a map with a workshop.
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/crafting",
                       data={"code": code, "quantity": quantity})

    @waitable
    def bank_deposit_gold(self, quantity: int) -> Response:
        """
        Deposit gold in a bank on the character's map.
        :param quantity: amount of gold
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/deposit/gold",
                       data={"quantity": quantity})

    @waitable
    def bank_deposit_items(self, deposit: dict[str, int]) -> Response:
        """
        Deposit multiple items in a bank on the character's map.
        The cooldown will be 3 seconds multiplied by the number of different items withdrawn.
        :param deposit: items and their amount. Like  {item_code: quantity, ...}
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/deposit/item",
                       data=[{"code": item_code, "quantity": quantity} for item_code, quantity in deposit.items()])

    @waitable
    def bank_withdraw_gold(self, quantity: int) -> Response:
        """
        Withdraw gold from your bank.
        :param quantity: amount of gold
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/withdraw/gold",
                       data={"quantity": quantity})

    @waitable
    def bank_withdraw_items(self, withdraw: dict[str, int]) -> Response:
        """
        Take items from your bank and put them in the character's inventory.
        The cooldown will be 3 seconds multiplied by the number of different items withdrawn.
        :param withdraw: items and their amount. Like  {item_code: quantity, ...}
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/withdraw/item",
                       data=[{"code": item_code, "quantity": quantity} for item_code, quantity in withdraw.items()])

    @waitable
    def bank_buy_expansion(self) -> Response:
        """
        Buy a 25 slots bank expansion.
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/buy_expansion")

    @waitable
    def npc_buy(self, code: str, quantity: int) -> Response:
        """
        Buy an item from an NPC on the character's map.
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/npc/buy",
                       data={"code": code, "quantity": quantity})

    @waitable
    def npc_sell(self, code: str, quantity: int) -> Response:
        """
        Sell an item to an NPC on the character's map.
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/npc/sell",
                       data={"code": code, "quantity": quantity})

    @waitable
    def ge_buy_item(self, ge_id: str, quantity: int) -> Response:
        """
        Buy an item at the Grand Exchange on the character's map.
        :param ge_id: Grand Exchange order ID
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/grandexchange/buy",
                       data={"id": ge_id, "quantity": quantity})

    @waitable
    def ge_create_sell_order(self, code: str, quantity: int, price: int) -> Response:
        """
        Create a sell order at the Grand Exchange on the character's map.
        Please note there is a 3% listing tax, charged at the time of posting, on the total price.
        :param code: item code name
        :param quantity: amount of item
        :param price: price in gold to your item
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/grandexchange/sell",
                       data={"code": code, "quantity": quantity, "price": price})

    @waitable
    def ge_cancel_sell_order(self, ge_id) -> Response:
        """
        Cancel a sell order at the Grand Exchange on the character's map.
        :param ge_id: Grand Exchange order ID
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/grandexchange/cancel",
                       data={"id": ge_id})

    @waitable
    def task_complete(self) -> Response:
        """
        Complete current Task
        :return: requests.Response
        """
        return request("POST", f"/my/{self.name}/action/task/complete")

    @waitable
    def task_exchange(self) -> Response:
        """
        Exchange 6 tasks coins for a random reward. Rewards are exclusive items or resources.
        :return: requests.Response
        """
        return request("POST", f"/my/{self.name}/action/task/exchange")

    @waitable
    def task_new(self) -> Response:
        """
        Accepting a new task.
        :return: requests.Response
        """
        return request("POST", f"/my/{self.name}/action/task/new")

    @waitable
    def task_new(self) -> Response:
        """
        Cancel a task for 1 tasks coin.
        :return: requests.Response
        """
        return request("POST", f"/my/{self.name}/action/task/cancel")

    @waitable
    def task_master_trade(self, code: str, quantity: int) -> Response:
        """
        Trading items with a Tasks Master.
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/task/trade",
                       data={"code": code, "quantity": quantity})

    @waitable
    def delete_item(self, code: str, quantity: int) -> Response:
        """
        Delete an item from your character's inventory.
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/delete",
                       data={"code": code, "quantity": quantity})

    @waitable
    def change_skin(self, skin: str) -> Response:
        """
        Change the skin of your character.
        :param skin: skin code
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/change_skin",
                       data={"skin": skin})

    @waitable
    def give_gold(self, quantity: int, character_name: str) -> Response:
        """
        Give gold to another character in your account on the same map.
        :param quantity: amount of gold.
        :param character_name: Target character's name
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/give/gold",
                       data={"quantity": quantity, "character": character_name})

    @waitable
    def give_item(self, items: list[dict[str, Any]], character_name: str) -> Response:
        """
        Give items to another character in your account on the same map.
        The cooldown will be 3 seconds multiplied by the number of different items given.
        :param items: list of items. Like [{"code": str, "quantity": 1}, ...]
        :param character_name: Target character's name
        :return: requests.Response
        """
        return request("POST",
                       f"/my/{self.name}/action/give/item",
                       data={"items": items, "character": character_name})
