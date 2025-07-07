import asyncio

from game.player.character import Character
from utils.request import request

class Game:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.characters = {d["name"]: Character(data=d)
                          for d in request("GET", "/my/characters").json()["data"]}

    @classmethod
    def start(cls):
        """
        This is for start the game. This function is blocking.
        """
        asyncio.get_event_loop().run_forever()

    @classmethod
    def create_character(cls, name: str, skin: str):
        """
        Create a character for the account
        :param name: str, Name of the future character
        :param skin: str, skin code
        """
        r = request("POST", "characters/create", data={"name": name, "skin": skin})
        if r.status_code == 200:
            cls._instance.characters[name] = Character(r.json()["data"])
