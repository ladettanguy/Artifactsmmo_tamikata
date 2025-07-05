from typing import Any

from utils.request import request_all_pages, request


class Bank:

    @staticmethod
    def get_bank_item_info() -> list[dict[str, Any]]:
        """
        Fetch all items in your bank.
        :return: list of items bank storage, like:
            [{"code": "string", "quantity": 1}, ...]
        """
        return request_all_pages("GET", "/my/bank/items")

    @staticmethod
    def get_bank_info() -> dict[str, int]:
        """
        Fetch bank details.
        :return: dict[str, int] like: {"slots": 0, "expansions": 0, "next_expansion_cost": 0, "gold": 0}
        """
        return request("GET", "/my/bank").json()["data"]
