import requests


def get_request(url):
    statuscode = requests.get(url)
    return statuscode.status_code
