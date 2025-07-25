from fastapi import APIRouter
from  APP.utils.db_utils import get_all_plans


router = APIRouter()

@router.get("/")
async def fetch_plans():
    return {"plans": get_all_plans()}
