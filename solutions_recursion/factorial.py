def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


def test_factorial():
    print('Testing... ')
    # start test
    assert factorial(0) == 1
    # end test
    print('Tests done successfully! Nice!')


test_factorial()