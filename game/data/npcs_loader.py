# Python script to update json with the same name

import json
import os

from game.data.dataloader import DataLoader
from game.data.updater import Updater
from utils.flexible_dict import FlexibleDict
from utils.request import request_all_pages


class NPCsLoader(Updater, DataLoader):

    data_file = "./json/npcs.json"

    @staticmethod
    def load():
        path = os.path.join(os.path.dirname(__file__), NPCsLoader.data_file)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def update():

        list_npc = request_all_pages("GET", "/npcs/details")

        result = FlexibleDict()
        for npc in list_npc:
            new_npc = npc.copy()
            new_npc.pop('name')
            new_npc.pop('code')
            result[npc['code']] = FlexibleDict(new_npc)

        list_npc = request_all_pages("GET", "/npcs/items")
        for npc in list_npc:
            new_npc = npc.copy()
            new_npc.pop('npc')
            try:
                result[npc['npc']]["shop"].append(new_npc)
            except KeyError:
                result[npc['npc']]["shop"] = [new_npc]


        formatted_json = json.dumps(result, indent=4, ensure_ascii=False)

        path = os.path.join(os.path.dirname(__file__), NPCsLoader.data_file)

        with open(path, "w", encoding="utf-8") as f:
            f.write(formatted_json)
