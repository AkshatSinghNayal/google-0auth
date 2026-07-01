# google-0auth

Reusable Google OAuth 2.0 module for FastAPI.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
```

Get credentials from the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) — create an OAuth 2.0 Client ID with **Authorized redirect URIs** set to `http://localhost:8000/auth/google/callback`.

## Usage

```python
from fastapi import FastAPI
from google_oauth import router

app = FastAPI()
app.include_router(router)
```

### Endpoints

| Method | Path                    | Description                          |
| ------ | ----------------------- | ------------------------------------ |
| GET    | `/auth/google/login`    | Redirects user to Google consent     |
| GET    | `/auth/google/callback` | Handles OAuth callback, returns user |

### Protect a route

```python
from fastapi import FastAPI, Depends
from google_oauth import router, get_current_user, GoogleUser

app = FastAPI()
app.include_router(router)

@app.get("/me")
async def me(user: GoogleUser = Depends(get_current_user)):
    return user
```

Send the Google ID token as a `Bearer` token in the `Authorization` header:

```
Authorization: Bearer <id_token>
```

## Module structure

```
google_oauth/
├── __init__.py         # Public exports
├── config.py           # Settings via pydantic-settings
├── schemas.py          # GoogleUser model
├── exceptions.py       # GoogleOAuthError
├── client.py           # authlib OAuth client
├── router.py           # Login / callback routes
└── dependencies.py     # Token verification dependency
```
