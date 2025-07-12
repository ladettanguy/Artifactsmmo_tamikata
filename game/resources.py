from typing import Any

from game.data.resources_loader import ResourcesLoader
from game.maps import Maps


class Resources:

    _resources = ResourcesLoader.load()

    @classmethod
    def get_map_resource(cls, resource_code):
        for code, resource_info in cls._resources.items():
            if resource_code in resource_info["drops"]:
                return Maps.POINT_OF_INTEREST.resource[code]
        return None

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
