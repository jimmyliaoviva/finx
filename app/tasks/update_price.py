# Keep your tasks in tasks.py small and readable
# Don't place your business logic in it, just import them here

from app.tasks.celery import app
from time import sleep

@app.task()
def update_tw_price() -> None:
    pass