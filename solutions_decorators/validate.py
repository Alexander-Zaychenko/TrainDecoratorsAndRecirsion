def validate_int(func):
    def inner(*args):
        for i in args:
            if not isinstance(i, int):
                return TypeError
        return func(*args)
    return inner


@validate_int
def example(a, b):
    return a * b


def test():
    assert example("a", 5) == TypeError
    assert example(2, 5) == 10
    print("Test ok")


test()
