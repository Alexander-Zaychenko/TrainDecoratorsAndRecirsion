def uppercase(func):
    def inner(*args, **kwargs):
        word = func()
        result = uppercase(word)

        return result
    return inner

@uppercase
def create_str():
    print('adsdasdsad')


create_str()