def uppercase(func):
    def inner(*args, **kwargs):
        word = func(*args, **kwargs)
        result = word.upper()

        return result
    return inner
