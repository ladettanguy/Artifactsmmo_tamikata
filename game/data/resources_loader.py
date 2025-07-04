# Python script to update json with the same name

import json
import os

from game.data.dataloader import DataLoader
from game.data.updater import Updater
from utils.request import request_all_pages


class ResourcesLoader(Updater, DataLoader):

    data_file = "./json/resources.json"

    @staticmethod
    def load():
        path = os.path.join(os.path.dirname(__file__), ResourcesLoader.data_file)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def update():

        list_resources = request_all_pages("GET", "/resources")

        result = {}
        for resource in list_resources:
            new_resource = resource.copy()
            new_resource.pop('name')
            new_resource.pop('code')
            result[resource['code']] = new_resource

        formatted_json = json.dumps(result, indent=4, ensure_ascii=False)

        path = os.path.join(os.path.dirname(__file__), ResourcesLoader.data_file)

        with open(path, "w", encoding="utf-8") as f:
            f.write(formatted_json)
