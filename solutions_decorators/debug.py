def debug(func):
    def inner(*args, **kwargs):
        print("Вызов функции:", func.__name__)
        print("Аргументы:", args, kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result
    return inner


# how to test that???

@debug
def debug_this(a):
    return a + 2.623423

debug_this(1)
