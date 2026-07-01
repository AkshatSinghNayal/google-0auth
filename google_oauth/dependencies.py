from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token

from .config import GoogleOAuthSettings
from .schemas import GoogleUser

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    settings: GoogleOAuthSettings = Depends(),
) -> GoogleUser:
    try:
        info = id_token.verify_oauth2_token(
            credentials.credentials,
            google_requests.Request(),
            settings.google_client_id,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {exc}",
        )
    return GoogleUser(
        id=info["sub"],
        email=info["email"],
        name=info.get("name"),
        picture=info.get("picture"),
    )
