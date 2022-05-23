
async def all_users():
    return "Student list"


async def show_user(id: int):
    return id


async def store_user():
    return "Student will store"


async def update_user(id: int):
    return "{id} student will update."


async def destroy_user(id: int):
    return "{id} student will delete."
