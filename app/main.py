from fastapi import FastAPI

from .api import api


from .ui import ui

app = FastAPI()


app.include_router(api.router)
app.include_router(ui.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

# This is for testing purposes, please keep
@app.get("/helloworld")
async def helloworld():
    return {"message": "Hello World!"}