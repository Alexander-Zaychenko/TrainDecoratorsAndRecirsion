def uppercase(func):
    def inner(*args, **kwargs):
        word = func()
        result = uppercase(word)

        return result
    return inner
