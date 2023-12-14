import redis

# 创建 Redis 客户端连接
redis_client = redis.Redis(
    host='localhost',  # Redis 服务器地址
    port=6379,          # Redis 服务器端口
    db=0,               # 使用的数据库编号
    decode_responses=True  # 如果设置为True，获取的数据将会是字符串而不是 bytes，默认为False
)

# # 通过 ping 测试连接是否正常
# response = redis_client.ping()
# print("Ping Response:", response)


# res = redis_client.set('name', 'haha321')

res = redis_client.keys()
for i in res:
    r = redis_client.get(i)
    print(r)


redis_client.flushdb()
