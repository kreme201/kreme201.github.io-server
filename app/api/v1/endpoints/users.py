from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_users():
    return {"action": "get all users"}


@router.post("/")
async def create_new_user():
    return {"action": "create new user"}


@router.get("/me")
async def get_self():
    return {"action": "get self info"}


@router.put("/me")
async def update_self():
    return {"action": "update user info self"}


@router.delete("/me")
async def delete_self():
    return {"action": "delete user self"}


@router.get("/{user_id}")
async def get_by_id(user_id: int):
    return {"action": "get self info", "user_id": user_id}


@router.put("/{user_id}")
async def update_by_id(user_id: int):
    return {"action": "update user info self", "user_id": user_id}


@router.delete("/{user_id}")
async def delete_by_id(user_id: int):
    return {"action": "delete user self", "user_id": user_id}
