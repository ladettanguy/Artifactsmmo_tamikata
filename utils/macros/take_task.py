import requests

from game.maps import Maps


def take_task(character: "Character", task_type: str) -> requests.Response:
    """
    take task to the correct Tasks Master
    :param character: Character object
    :param task_type: str, task type "monsters" or "items"
    :return: requests.Response
    """
    character.action.move(*Maps.POINT_OF_INTEREST.tasks_master[task_type])
    return character.action.task_new()
