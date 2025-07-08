import time
from utils.request import calculate_real_cooldown

def waitable(fn):
    def wrapper(*args, wait=True, **kwargs):
        r = fn(*args, **kwargs)
        if r and wait and r.status_code == 200:
            time.sleep(calculate_real_cooldown(r.json()["data"]["cooldown"]["expiration"]))
        return r

    return wrapper
