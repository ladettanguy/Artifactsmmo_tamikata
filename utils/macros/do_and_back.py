from typing import Callable

import requests


def do_and_back(character: "Character", fn: Callable, *args, **kwargs) -> requests.Response:
    x, y = character.get_position()
    r = fn(*args, **kwargs)
    character.action.move(x, y)
    return r
