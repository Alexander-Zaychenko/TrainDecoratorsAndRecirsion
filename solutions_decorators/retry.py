def retry(times=3):
    def decorator(func):
        count = 1
        def inner(*args, **kwagrs):
            nonlocal count
            try:
                result = func(*args, **kwagrs)
            except Exception as e:
                if count < times:
                    count += 1
                    return inner(*args, **kwagrs)
                return e
            return result
        return inner
    return decorator


@retry(times=4)
def function():
    print('hi')

function()