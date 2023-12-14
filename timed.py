from app import cel
from celery.schedules import crontab


# 配置定时任务
cel.conf.beat_schedule = {
    'my_task': {
        'task': 'task_1.my_task',  # 任务函数的路径
        'schedule': crontab(minute='*/1'),  # 定时规则 每分钟执行一次
    },
    'add_task': {
        'task': 'task_1.add_1',  # 任务函数的路径
        'schedule': 5,  # 定时规则 每5秒执行一次
        'args': (4, 5)
    },
}


