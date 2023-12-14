from task_1 import add_1
from task_2 import add_2

# from celery.result import AsyncResult
from app import cel
import time

add_1_task = add_1.delay(9, 3)
add_2_task = add_2.delay(4, 3)


# asyn_cresult = AsyncResult(id=send_sms_task.id, app=cel)
# while 1:
#     print(asyn_cresult.status)
#     time.sleep(0.5)
#     if asyn_cresult.status == "SUCCESS":
#         print(asyn_cresult.status)  # 获取状态
#         print(asyn_cresult.get())  # 获取结果
#         break


