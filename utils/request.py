import os
import requests

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
