from fastapi import APIRouter

from app.tasks.hello_world import hello_world 

router = APIRouter(    
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},)


@router.get("/hello")
async def hello():
    return {"message": "Hello to the API!"}

@router.get("/celery-example")
def celery_example():
    # TODO: should implement factory pattern here
    try:
        hello_world.delay()
    except Exception as e:
        return {"message":f"fail to update, exception: {e}"}
    return {"message": "helllo world with worker"}