def validate(func, arg):
    def inner(*args, **kwwargs):
        if func(arg):
            return True
        return False
    return inner
