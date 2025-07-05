from typing import Callable

import requests


def do_and_back(character: "Character", fn: Callable, *args, **kwargs) -> requests.Response:
    """
    Do a function and back to the original position
    :param character: Character object
    :param fn: Callable, function to call
    :param args: args to pass to fn
    :param kwargs: kwargs to pass to fn
    :return: requests.Response
    """
    x, y = character.get_position()
    r = fn(*args, **kwargs)
    character.action.move(x, y)
    return r
