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


def sum_list(arr):
    if not arr:
        return 0
    current = arr[0]
    if current < 0:
        current = 0
    return current + sum_list(arr[1:])


@timer
def test_sum_list():
    print('Testing... ')
    # create constants of solutions
    LIST_1 = []
    LIST_2 = list(range(1, 100))
    LIST_3 = list(range(1, 100))[::2]
    LIST_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # start test
    assert sum_list(LIST_1) == sum(LIST_1)
    assert sum_list(LIST_2) == sum(LIST_2)
    assert sum_list(LIST_3) == sum(LIST_3)
    assert sum_list(LIST_4) == sum(LIST_4)
    # end test
    print('Tests done successfully! Nice!')


test_sum_list()