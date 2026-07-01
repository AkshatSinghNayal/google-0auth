from pydantic_settings import BaseSettings


class GoogleOAuthSettings(BaseSettings):
    google_client_id: str = ""
    google_client_secret: str = ""
    google_redirect_uri: str = "http://localhost:8000/auth/google/callback"
    google_scopes: list[str] = ["openid", "email", "profile"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}
