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


def factorial(number):
    if number == 0:
        return 1
    if number == 1:
        return number
    return number * factorial(number - 1)


@timer
def test_factorial():
    print('Testing... ')
    # create constants of solutions
    FAC_94 = 108736615665674308027365285256786601004186803580182872307497374434045199869417927630229109214583415458560865651202385340530688000000000000000000000
    FAC_163 = 2004401576545302577599591653441552787812849977066285969791842909503537700391898214353410600501293996807267197132074467682448564494675371562796423038301229264886150247730010662205704969956173185881152129393638460096840367667292791327201696065980922331136000000000000000000000000000000000000000
    # start test
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(94) == FAC_94
    assert factorial(163) == FAC_163
    # end test
    print('Tests done successfully! Nice!')


test_factorial()