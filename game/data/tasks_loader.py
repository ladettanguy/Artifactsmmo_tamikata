# Python script to update json with the same name

import json
import os

from game.data.dataloader import DataLoader
from game.data.updater import Updater
from utils.request import request_all_pages


class TasksLoader(Updater, DataLoader):

    data_file = "./json/tasks.json"

    @staticmethod
    def load():
        path = os.path.join(os.path.dirname(__file__), TasksLoader.data_file)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def update():

        list_tasks = request_all_pages("GET", "/tasks/list")

        result = {}
        for tasks_info in list_tasks:
            new_item = tasks_info.copy()
            new_item.pop('code')
            result[tasks_info["code"]] = new_item

        formatted_json = json.dumps(result, indent=4, ensure_ascii=False)

        path = os.path.join(os.path.dirname(__file__), TasksLoader.data_file)

        with open(path, "w", encoding="utf-8") as f:
            f.write(formatted_json)
