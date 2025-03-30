from celery import Celery

app = Celery("tasks", broker_url='amqp://localhost:5672',
result_expires=3600,
task_serializer='json',
result_serializer='json',
accept_content=['json'],
timezone='Asia/Taipei',
enable_utc=True)

app.conf.imports = [
    'app.tasks.update_data_tasks',
    'app.tasks.hello_world']

if __name__ == '__main__':
    app.start()