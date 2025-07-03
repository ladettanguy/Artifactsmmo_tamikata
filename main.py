from game.game import get_characters
from game.scenario.farm_gathering import farm_gathering
from threading import Thread


characters = get_characters()
# c1 = characters.pop("tamikata1")
threads = []

for character in characters.values():
    t = Thread(target=farm_gathering, args=(character, (-1, 0)), daemon=True)
    threads.append(t)
    t.start()


# wait thread
for t in threads:
    t.join()
