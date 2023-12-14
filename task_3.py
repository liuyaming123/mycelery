import redis
from app import cel

# 创建 Redis 客户端连接
redis_client = redis.Redis(
    host='localhost',  # Redis 服务器地址
    port=6379,          # Redis 服务器端口
    db=0,               # 使用的数据库编号
    decode_responses=True  # 如果设置为True，获取的数据将会是字符串而不是 bytes，默认为False
)

@cel.task
def redis_flush():
    redis_client.flushdb()
