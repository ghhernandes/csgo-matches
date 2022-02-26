import redis

r = redis.Redis(
    host='hostname',
    port=0, 
    password='password')