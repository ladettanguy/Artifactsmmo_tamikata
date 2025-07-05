from typing import Any

from game.data.maps_loader import MapsLoader


class Resources:

    _resources = MapsLoader.load()

    @classmethod
    def get(cls, resources_code: str) -> dict[str, Any]:
        """
        Get resources information
        :param resources_code: str, resources code
        :return: dict[str, Any] like:
        {
            "skill": "woodcutting",
            "level": 1,
            "drops": [{"code": "sap", "rate": 10, "min_quantity": 1, "max_quantity": 1}, ...],
        }
        """
        return cls._resources[resources_code]
