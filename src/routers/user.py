
from fastapi import APIRouter
from src.controllers.user import *

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def index():
    return await all_users()


@router.get("/{id}")
async def show(id: int):
    return await show_user(id)


@router.post("/")
async def store():
    return await store_user()


@router.put("/{id}")
async def update(id: int):
    return await update_user(id)


@router.delete("/{id}")
async def destroy(id: int):
    return await destroy_user(id)
