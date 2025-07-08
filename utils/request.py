import requests
import math
import os

from typing import Any
from datetime import datetime, timezone


api_key = os.environ.get('ARTIFACTS_KEY', None) or exit()
server = "https://api.artifactsmmo.com/"

def request(method: str, endpoint: str, data=None) -> requests.Response:
    """
    Send a request to artifacts api
    :param method: http method
    :param endpoint: endpoint to build url
    :return: requests.Response object
    """
    url = server + endpoint
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    return requests.request(method, url, json=data, headers=headers)

def request_all_pages(method: str, endpoint: str, data=None) -> list[dict[str, Any]]:
    info = request(method, endpoint, data).json()
    i = info["page"]
    result: list[dict[str, Any]] = info["data"]
    while i <= info["pages"]:
        info = request(method, endpoint+f"?page={i+1}", data).json()
        result.extend(info["data"])
        i = info["page"]
    return result

def calculate_real_cooldown(expiration_date):
    date_str = expiration_date.replace("Z", "+00:00")
    date = datetime.fromisoformat(date_str)
    return max(math.ceil((date - datetime.now(timezone.utc)).total_seconds()), 0)