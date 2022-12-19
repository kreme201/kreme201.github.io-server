from fastapi import APIRouter

router = APIRouter()


@router.post("/access-token")
async def get_access_token():
    return {"action": "get access token"}


@router.post("/password-recovery/{email}")
async def send_password_recovery(email: str):
    return {"action": "send password recovery", "email": email}


@router.post("/password-reset")
async def password_reset(password: str):
    return {"action": "password reset", "password": password}
