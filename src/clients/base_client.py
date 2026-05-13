import requests
import os

class BaseClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://api.escuelajs.co/api/v1")

        # using session TCP
        self.session = requests.Session()

        # standart header
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _send_request(self, method, endpoint, **kwargs):
        """
        Private method for handle all requests
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.request(method, url, **kwargs)
            # raise erorr network server (4xx,5xx)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise
    
    def get(self, endpoint, params=None, **kwargs):
        """
        Method for GET request
        """
        return self._send_request("GET", endpoint, params=params, **kwargs)
    
    def post(self, endpoint, json=None, **kwargs):
        """
        Method for POST request
        """
        return self._send_request("POST", endpoint, json=json, **kwargs)
    
    def put(self, endpoint, json=None, **kwargs):
        """
        Method for PUT request
        """
        return self._send_request("PUT", endpoint, json=json, **kwargs)