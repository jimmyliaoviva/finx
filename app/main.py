from fastapi import Depends, FastAPI


from .routers import api, ui

app = FastAPI()


app.include_router(api.router)
app.include_router(ui.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}