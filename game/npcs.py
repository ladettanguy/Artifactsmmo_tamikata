from typing import Optional, Any

from game.data.npcs_loader import NPCsLoader


class NPCs:

    _npcs = NPCsLoader.load()


    @classmethod
    def search_item_vendor(cls, item_code: str) -> Optional[str]:
        """
        Search which npc buy or sell a item
        :param item_code: Item code wanted
        :return: str, npc code
        """
        for npc_code, npc_info in cls._npcs.items():
            try:
                for item in npc_info["shop"]:
                    if item["code"] == item_code:
                        return npc_code
            except KeyError:
                continue
        return None

    @classmethod
    def get(cls, npcs_code: str) -> dict[str, Any]:
        """
        Get npc information
        :param npcs_code: str, npc code
        :return: Dict[str, Any] like:
        {
            "description": "Description text ipsum",
            "type": "trader",
            "shop": [{"code": "topaz_book", "currency": "elemental_page", "buy_price": 30, "sell_price": null}, ...]
        }
        """
        return cls._npcs[npcs_code]
