from fastapi import APIRouter
from app.tasks.hello_world import hello_world 
from app.database import TaiwanStockInfo, session_scope
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

@router.get("/database-example")
def database_example():
    try:
        with session_scope() as session:
            all_tw=TaiwanStockInfo.get_all_tw_stock_info(session)
        print(all_tw)
    except Exception as e:
        print(f"fail to update, exception: {e}")
        return {"message":f"fail to update, exception: {e}"}
    return {"message": "query database successfully"}