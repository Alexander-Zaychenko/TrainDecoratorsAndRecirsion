def retry(func, times):
    def inner(*args, **kwagrs):
        for i in range(times):
            func()
        return times
    return inner
