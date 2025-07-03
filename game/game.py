from typing import Any

from game.scenario.nothing_to_do import NothingToDo
from game.scenario.scenario import Scenario
from game.player.character import Character
from utils.request import request
from utils.thread_scenario import ThreadScenario


class Game:

    def __init__(self):
        self.character = self.get_characters()
        self.character_thread: dict[str, ThreadScenario] = {c: ThreadScenario(NothingToDo, c) for c in self.character.keys()}

    def set_scenario(self, character_name: str, scenario: type[Scenario], args=(), start=False):
        """

        :param character_name:
        :param scenario:
        :param args:
        :param start:
        :return:
        """
        if self.character_thread[character_name].is_alive():
            self.character_thread[character_name].cancel()

        self.character_thread[character_name] = ThreadScenario(scenario, name=character_name, args=args)
        if start:
            self.character_thread[character_name].start()

    def start(self):
        """
        This is for start the game. This function is blocking.
        """
        for ct in self.character_thread.values():
            ct.start()

        # It's gonna be replace by the asyncio loop who schedule the websocket
        for ct in self.character_thread.values():
            ct.join()

    def run(self):
        """
        This fort start the game. This function is not blocking.
        """
        pass

    @staticmethod
    def create_character(name: str, skin: str) -> Character:
        r = request("POST", "characters/create", data={"name": name, "skin": skin})
        if r.status_code != 200:
            return

        return Character(r.json()["data"])

    @staticmethod
    def get_characters() -> dict[str, Character]:
        """
        use to have a spécific character from his name
        :param name: character's name
        :return: Character or None
        """
        return {d["name"]: Character(data=d) for d in request("GET", "/my/characters").json()["data"]}

    @staticmethod
    def get_bank_item_info() -> dict[str, Any]:
        """
        Get items bank storage
        :return: Dictionary of items bank storage
        """
        return request("GET", "/my/bank/items").json()["data"]