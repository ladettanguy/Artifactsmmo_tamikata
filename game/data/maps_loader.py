# Python script to update json with the same name

import json
import os

from game.data.dataloader import DataLoader
from game.data.updater import Updater
from utils.request import request_all_pages


class MapsLoader(Updater, DataLoader):

    data_file = "./json/maps.json"

    @staticmethod
    def load():
        path = os.path.join(os.path.dirname(__file__), MapsLoader.data_file)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def update():

        list_maps = request_all_pages("GET", "/maps")

        result = {}
        for map_info in list_maps:
            new_map = map_info.copy()
            new_map.pop('x')
            new_map.pop('y')
            result[str(map_info['x']) + ' ' + str(map_info['y'])] = new_map

        formatted_json = json.dumps(result, indent=4, ensure_ascii=False)

        path = os.path.join(os.path.dirname(__file__), MapsLoader.data_file)

        with open(path, "w", encoding="utf-8") as f:
            f.write(formatted_json)
