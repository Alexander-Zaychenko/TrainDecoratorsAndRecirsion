def sum_list(arr):
    if not arr:
        return 0
    current = arr[0]
    if current < 0:
        current = 0
    return current + sum_list(arr[1:])
