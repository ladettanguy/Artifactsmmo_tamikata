import time

def waitable(fn):
    def wrapper(*args, wait=True, **kwargs):
        r = fn(*args, **kwargs)
        if wait and r.status_code == 200:
            time.sleep(r.json()["data"]["cooldown"]["remaining_seconds"])
        return r

    return wrapper
