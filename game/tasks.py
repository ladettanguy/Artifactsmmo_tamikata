from typing import Any

from game.data.tasks_loader import TasksLoader
from game.maps import Maps


class Tasks:

    _tasks = TasksLoader.load()


    @classmethod
    def get(cls, task_code: str):
        """
        Get task information
        :param task_code: str, Task code
        :return: dict[str, Any] like:
        {
            "level": 1,
            "type": "monsters",
            "min_quantity": 50,
            "max_quantity": 400,
            "skill": null,
            "rewards": {
                "items": [{"code": "tasks_coin", "quantity": 3}],
                "gold": 200
            }
        }
        """
        return cls._tasks[task_code]