def fibonacci(n):
    # check low nums
    if n < 0:
        return ValueError
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci():
    print('Testing... ')
    # start test
    assert fibonacci(6) == 8
    assert fibonacci(12) == 144
    assert fibonacci(14) == 377
    assert fibonacci(22) == 17711
    assert fibonacci(-2) == ValueError
    # end test
    print('Tests done successfully! Nice!')


test_fibonacci()