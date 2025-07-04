from typing import Optional

from game.data.maps_loader import MapsLoader


class NPCs:

    _npcs = MapsLoader.load()


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
    def __getattr__(cls, item):
        return cls[item]

    @classmethod
    def __getitem__(cls, item):
        return cls._npcs[item]
