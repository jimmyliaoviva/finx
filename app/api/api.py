from fastapi import APIRouter

router = APIRouter(    
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},)


@router.get("/hello")
async def read_root():
    return {"message": "Hello to the API!"}