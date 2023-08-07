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
