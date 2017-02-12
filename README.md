# store data temporary

Usage:
> # store value
> sh $ curl -d 'data=test-data' http://localhost:8000/set/test-key/
> # get value
> sh $ curl http://localhost:8000/get/test-key/

Variables in settings.py
> REDIS_HOST = 'localhost'

> REDIS_PORT = 6379

> REDIS_DB = 0

> REDIS_KEY_EXPIRE_TIME = 3600

