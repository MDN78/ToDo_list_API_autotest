import requests
from utils.logger import Logger

"""Http method's list"""

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def patch(url, body):
        Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result
