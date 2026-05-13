from src.clients.base_client import BaseClient
from src.endpoints.auth_endpoint import AuthEndpoint

class AuthService(BaseClient):
    def __init__(self):
        super().__init__()
        self.endpoint_login = AuthEndpoint.LOGIN
        self.enpoint_profile = AuthEndpoint.PROFILE

    def auth(self, json):
        return self.post(self.endpoint_login, json)

    def profile(self, headers=None):
        return self.get(self.enpoint_profile, headers=headers)