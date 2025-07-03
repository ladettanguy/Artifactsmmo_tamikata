from typing import Any

from requests import Response
from utils.request import request
from utils.decorator import waitable

class Action:

    def __init__(self, name):
        self.name = name

    @waitable
    def move(self, x: int, y: int) -> Response:
        """
        Use to move the character at the [x, y] tile
        :param x: X Coordinate of wanted tile
        :param y: Y Coordinate of wanted tile
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/move",
                       data={"x": x, "y": y})

    @waitable
    def fight(self) -> Response:
        """
        Use to fight on the character's tile
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/fight")

    @waitable
    def rest(self) -> Response:
        """
        Use to rest the character and regen some HP
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/rest")

    @waitable
    def gathering(self) -> Response:
        """
        Use to gather resources on character's tile
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/gathering")

    @waitable
    def recycling(self, code: str, quantity: int) -> Response:
        """
        Use to recycle an item on a workshop tile
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
        Use an item in character's inventory
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
        Use to equip an item in a character's slot
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
        Use to unequip an item in a character's slot
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
        use to craft some item (care to be in the appropriate tile)
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
        use to deposit gold in a bank
        :param quantity: amount of gold
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/deposit/gold",
                       data={"quantity": quantity})

    @waitable
    def bank_deposit_item(self, deposit: list[dict[str, Any]]) -> Response:
        """
        use to deposit item in a bank
        :param deposit: items and their amount. Like [{"code": item_code, "quantity": quantity}, ...]
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/deposit/item",
                       data=deposit)

    @waitable
    def bank_withdraw_gold(self, quantity: int) -> Response:
        """
        use to recover gold from bank
        :param quantity: amount of gold
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/withdraw/gold",
                       data={"quantity": quantity})

    @waitable
    def bank_withdraw_item(self, code: str, quantity: int) -> Response:
        """
        use to recover item from bank
        :param code: item code name
        :param quantity: amount of item
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/withdraw/item",
                       data={"code": code, "quantity": quantity})

    @waitable
    def bank_buy_expansion(self) -> Response:
        """
        use to buy expansion from bank
        :return: requests.Response
        """
        return request("POST",
                       f"my/{self.name}/action/bank/buy_expansion")