from fastapi import APIRouter

router = APIRouter(    
    prefix="/ui",
    tags=["ui"],
    responses={404: {"description": "Not found"}},)