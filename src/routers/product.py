
from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def index():
    return "products list"


@router.get("/{id}")
async def show():
    return {id+" products show"}


@router.post("/")
async def store():
    return "products will store"


@router.put("/{id}")
async def update():
    return {id+" will update"}


@router.delete("/{id}")
async def destroy():
    return {id+" will destroy"}
