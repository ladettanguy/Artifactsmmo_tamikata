from typing import Any

from utils.request import request_all_pages, request


class Bank:

    @staticmethod
    def get_bank_item_info() -> list[dict[str, Any]]:
        """
        Fetch all items in your bank.
        :return: list of items bank storage
        """
        return request_all_pages("GET", "/my/bank/items")

    @staticmethod
    def get_bank_info():
        """
        Fetch bank details.
        :return:
        """
        return request("GET", "/my/bank").json()["data"]
