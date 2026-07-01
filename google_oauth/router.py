from fastapi import APIRouter, Depends, Request
from starlette.responses import RedirectResponse

from .client import create_google_oauth
from .config import GoogleOAuthSettings
from .exceptions import GoogleOAuthError
from .schemas import GoogleUser

router = APIRouter(prefix="/auth/google", tags=["google-oauth"])


@router.get("/login")
async def login(request: Request, settings: GoogleOAuthSettings = Depends()):
    oauth = create_google_oauth(settings)
    redirect_uri = request.url_for("callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback", response_model=GoogleUser)
async def callback(request: Request, settings: GoogleOAuthSettings = Depends()):
    oauth = create_google_oauth(settings)
    token = await oauth.google.authorize_access_token(request)
    userinfo = token.get("userinfo")
    if not userinfo:
        raise GoogleOAuthError(detail="Failed to retrieve user info from Google")
    return GoogleUser(
        id=userinfo["sub"],
        email=userinfo["email"],
        name=userinfo.get("name"),
        picture=userinfo.get("picture"),
    )
