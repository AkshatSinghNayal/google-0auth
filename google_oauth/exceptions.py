from fastapi import HTTPException


class GoogleOAuthError(HTTPException):
    def __init__(self, detail: str = "Google OAuth error", status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)
