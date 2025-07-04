# Python script to update json with the same name

import json
import os

from game.data.dataloader import DataLoader
from game.data.updater import Updater
from utils.request import request_all_pages


class MonstersLoader(Updater, DataLoader):

    data_file = "./json/monsters.json"

    @staticmethod
    def load():
        path = os.path.join(os.path.dirname(__file__), MonstersLoader.data_file)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def update():

        list_monsters = request_all_pages("GET", "/monsters")

        result = {}
        for monster in list_monsters:
            new_monster = monster.copy()
            new_monster.pop('name')
            new_monster.pop('code')
            result[monster['code']] = new_monster

        formatted_json = json.dumps(result, indent=4, ensure_ascii=False)

        path = os.path.join(os.path.dirname(__file__), MonstersLoader.data_file)

        with open(path, "w", encoding="utf-8") as f:
            f.write(formatted_json)
