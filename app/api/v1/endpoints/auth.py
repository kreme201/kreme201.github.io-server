from fastapi import APIRouter

router = APIRouter()


@router.post("/access-token")
async def auth_access_token():
    return {"action": "Return AccessToken"}


@router.post("/password-recovery/{email}")
async def auth_password_recovery(email: str):
    return {"action": "Send Password Recovery Email", "email": email}


@router.post("/password-reset")
async def auth_password_reset():
    return {"action": "Reset Password"}
