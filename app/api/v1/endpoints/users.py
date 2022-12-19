from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_users():
    return {"action": "get users"}


@router.post("/")
async def create_user():
    return {"aciton": "create user"}


@router.get("/me")
async def get_user_self():
    return {"action": "get user self"}


@router.put("/me")
async def update_user_self():
    return {"action": "update user self"}


@router.delete("/me")
async def delete_user_self():
    return {"action": "delete user self"}


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return {"action": "get user by id", "user_id": user_id}


@router.put("/{user_id}")
async def update_user_by_id(user_id: int):
    return {"action": "update user by id", "user_id": user_id}


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int):
    return {"action": "delte user by id", "user_id": user_id}
