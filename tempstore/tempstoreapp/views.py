from django.shortcuts import render
from django.http import HttpResponse
from throttle.decorators import throttle
from django.conf import settings

import redis

REDIS_HOST = getattr(settings, "REDIS_HOST", 'localhost')
REDIS_PORT = getattr(settings, "REDIS_PORT", 6379)
REDIS_DB   = getattr(settings, "REDIS_DB", 0)
REDIS_KEY_EXPIRE_TIME = getattr(settings, "REDIS_KEY_EXPIRE_TIME", 60)

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def index(request):
    return HttpResponse("Its Works")

@throttle(zone='default')
def set(request, key):
    data = request.POST.get('value')
    r.setex(key,REDIS_KEY_EXPIRE_TIME,data)
    return HttpResponse("OK")    

@throttle(zone='default')
def get(request, key):
    data = r.get(key)
    return HttpResponse(data)    

