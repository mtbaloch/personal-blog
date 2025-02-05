from fastapi import APIRouter
from app.models.user_model import User

# creates router
router = APIRouter(prefix="/users", tags=["Users"])


# create user route
@router.post("/")
async def create_user():
    # write logic here
    pass