from celery import Celery
from celery.schedules import crontab
import time


cel = Celery('tasks',
             backend='redis://localhost:6379/0',  # 结果后端
             broker='redis://localhost:6379/1',  # 消息代理
             task_default_queue = 'custom_queue',  # 自定义队列名称
             broker_connection_retry_on_startup = True,
             timezone='Asia/Shanghai',
             include=['task_1', 'task_2', ],
        )
'''
启动worker: celery -A app worker --loglevel=info
-A 参数: 表示Celery对象所在的py文件的文件名
-l 参数:日志级别
-P 参数:表示事件驱动使用eventlet 这个在类Unix 平台不需要设置但在Windows 平台需要设置 并且eventlet 还要用 pip 单独安装
-c 参数:表示并发数量 比如再加上-c 10表示限制并发数量为 10
-D 启动 worker 默认是前台启动，加上 -D 会后台启动

如果修改了celery的工厂任务 要重新


启动定时任务时也要启动worker
celery -A app worker --loglevel=info
celery -A timed beat --loglevel=info
## 启动定时任务时， -A 后边的参数为配置定时任务所在的文件的文件名 即cel.conf.beat_schedule所在的文件名
'''



# # 配置定时任务
# cel.conf.beat_schedule = {
#     'my_task': {
#         'task': 'task_1.my_task',  # 任务函数的路径
#         'schedule': crontab(minute='*/1'),  # 定时规则 每分钟执行一次
#     },
#     'add_task': {
#         'task': 'task_1.add_1',  # 任务函数的路径
#         'schedule': 5,  # 定时规则 每5秒执行一次
#         'args': (4, 5)
#     },
# }
