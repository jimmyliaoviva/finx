# Description[WIP]

# Install
## Requirement
* python 3.11 
* pip
## Install packages

```sh
pip install -r requirements.txt
```


# Add new package to requirement

```sh
pipreqs  --ignore ".venv" --force 
```

# Services
## Start Rabbitmq container
```sh
sudo docker run -d -p 5672:5672 -p 8080:15672 rabbitmq:3-management
```
## Start a fastapi server
```sh
fastapi dev ./app/main.py
```

## start a celery worker
```sh
celery -A app.tasks.celery  worker
```

## openapi
http://localhost:8000/docs