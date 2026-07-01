from authlib.integrations.starlette_client import OAuth

from .config import GoogleOAuthSettings


def create_google_oauth(settings: GoogleOAuthSettings) -> OAuth:
    oauth = OAuth()
    oauth.register(
        name="google",
        client_id=settings.google_client_id,
        client_secret=settings.google_client_secret,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": " ".join(settings.google_scopes)},
    )
    return oauth
