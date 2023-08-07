import time

def timer(func):
    def inner(*args, **kwargs):
        start_time = time.monotonic()
        print(f'Start at: {start_time}')
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        print(f'End at: {end_time}')
        complete_time = end_time - start_time
        print(f'Complete time: {complete_time}')

        return result
    return inner


def fibonacci(n):
    # check low nums
    if n < 0:
        return ValueError
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
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