import time
from utils.request import calculate_real_cooldown

def waitable(fn):
    def wrapper(self, *args, **kwargs):
        time.sleep(self.character.get_cooldown())
        r = fn(self, *args, **kwargs)
        if r and r.status_code == 200:
            self.character.last_cooldown_expiration = r.json()["data"]["cooldown"]["expiration"]
        return r

    return wrapper
