from redis import Redis
import functools

redis_server = Redis(host='redis', port=6379)


def get_redis():
    return redis_server


def cache_for(time, key=None):
    """ Decorator to cache any function call for a given time.
    """

    def _cache_for(f):
        @functools.wraps(f)
        def _decorator(*args, **kwargs):
            _key = key
            result = None
            try:
                result = redis_server.get(_key)
            except Exception:
                pass
            if not result:
                result = f(*args, **kwargs)
                try:
                    redis_server.set(_key, result, ex=time)
                except Exception:
                    pass
            return result

        return _decorator

    return _cache_for


def set(*args, **kwargs):
    return redis_server.set(*args, **kwargs)


def get(*args, **kwargs):
    return redis_server.get(*args, **kwargs)


def exists(*args, **kwargs):
    return redis_server.exists(*args, **kwargs)
