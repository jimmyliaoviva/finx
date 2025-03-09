from app.tasks import update_data_tasks

def sync_all_tw_info():
    update_tw_info()
    update_tw_price()

def update_tw_info():
    update_data_tasks.update_tw_info_t()

def update_tw_price():
    pass
    update_data_tasks.update_tw_price_t()