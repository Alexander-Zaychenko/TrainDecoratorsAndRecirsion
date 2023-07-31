def debug(func):
    def wrapper(*args, **kwargs):
        print("Вызов функции:", func.__name__)
        print("Аргументы:", args, kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result
    return wrapper