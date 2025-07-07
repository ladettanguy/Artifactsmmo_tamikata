from typing import Any, Optional

from game.data.maps_loader import MapsLoader as _Maps
from utils.flexible_dict import FlexibleDict


class Maps:

    _map_loaded: dict[str, Any] = _Maps.load()
    POINT_OF_INTEREST = None

    @classmethod
    def refresh_point_of_interest(cls):
        """
        Refresh data for POINT_OF_INTEREST constant
        """
        _map_loaded: dict[str, Any] = _Maps.load()
        _set_type = {_map_info['content']['type']: FlexibleDict() for _map_info in _map_loaded.values() if
                     _map_info.get("content")}

        _point_of_interest = FlexibleDict(_set_type)

        for _coord, _map_info in _map_loaded.items():
            _content = _map_info.get("content", None)
            if not _content:
                continue

            if not _point_of_interest[_content["type"]].get(_content["code"], None):
                _x, _y = _coord.split(" ")
                _point_of_interest[_content["type"]][_content["code"]] = [int(_x), int(_y)]

        cls.POINT_OF_INTEREST = _point_of_interest

    @classmethod
    def get_all_map(cls) -> dict[str, dict[str, Any]]:
        """
        Fetch all map dictionary
        :return: Dict[str, Dict[str, Any] like:
        {
            "7 13": {"name": "Forest", "skin": "forest_bank2", "content": {"type": "bank", "code": "bank"},
            ...
        }
        """
        return cls._map_loaded

    @classmethod
    def get(cls, x, y) -> Optional[dict[str, Any]]:
        """
        Get map info of [x, y] tile
        :param x: coord x
        :param y: coord y
        :return: Optional[Dict[str, Any]] like:
        {
            "name": "Forest",
            "skin": "forest_bank2",
            "content": {
                "type": "bank",
                "code": "bank"
            }
        }
        """
        return cls._map_loaded.get(f"{x} {y}", None)


Maps.refresh_point_of_interest()
