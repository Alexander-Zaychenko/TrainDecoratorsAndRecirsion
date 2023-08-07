def uppercase(func):
    def inner(*args, **kwargs):
        word = func(*args, **kwargs)
        result = word.upper()

        return result
    return inner


@uppercase
def hello_text(string):
    return f"Hello {string}"


def test_uppercase():
    print('Testing... ')
    # start test
    assert hello_text('world') == "HELLO WORLD"
    assert hello_text('me') == "HELLO ME"
    assert hello_text('python') == "HELLO PYTHON"
    # end test
    print('Tests done successfully! Nice!')


test_uppercase()