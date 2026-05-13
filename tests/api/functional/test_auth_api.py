from src.models.auth_model import AuthLoginRequest, AuthLoginResponse, AuthProfileResponse
from src.services.auth_service import AuthService
from assertpy import assert_that
import pytest

class TestAuthApi:

    @pytest.mark.positive
    def test_auth_login(self, auth_service: AuthService):

        # Arrange: request payload (hardcode)
        payload = AuthLoginRequest(
            email="john@mail.com",
            password="changeme",
        )
        
        # Act: send login request
        response = auth_service.auth(payload.model_dump())

        # Assert: validate status code
        assert_that(response.status_code).is_equal_to(201)
        
        # Assert: mapping response to model
        data = AuthLoginResponse(**response.json())

        # Assert: validate response body
        assert_that(data.access_token).is_not_empty()
        assert_that(data.refresh_token).is_not_empty()
        assert_that(data.access_token).is_type_of(str)
        assert_that(data.access_token).starts_with("ey")
        assert_that(data.refresh_token).starts_with("ey")

    @pytest.mark.positive
    def test_auth_profile(self, auth_service: AuthService, accces_token):

        # Arrange: request headers
        headers = {
            "Authorization": f"Bearer {accces_token}"
        }
        
        # Act: send profile request
        response = auth_service.profile(headers=headers)
        
        # Assert: mapping response to model
        data = AuthProfileResponse(**response.json())

        # Assert: validate response body
        assert_that(data.id).is_not_none()
        assert_that(data.email).is_not_empty()