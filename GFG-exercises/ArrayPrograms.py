def sum_array(items):
    if len(items) == 0:
        return 0
    summed = 0
    for index in range(0, len(items)):
        summed += items[index]
    return summed


def find_largest(items):
    largest = 0
    for index in range(0, len(items)):
        if items[index] > largest:
            largest = items[index]
    return largest


def rotate_list(items, rotations):
    rotated = list(items)
    for rotation in range(0, rotations):
        rotated.append(rotated.pop(0))
    return rotated


def reverse_list(items):
    reverse = []
    n = len(items) - 1
    while n >= 0:
        reverse.append(items[n])
        n -= 1
    return reverse


def split_and_concat(items, position):
    items = items[position:len(items)] + items[0:position]
    return items


def remainder_array_multiplication(items, divisor):
    if len(items) == 0:
        return "list is empty"
    i = 0
    product = 1
    while i < len(items):
        product *= items[i]
        i += 1
    res = product % divisor
    return res


def is_monotonic(items):
    if len(items) == 0:
        return "list is empty"
    if len(items) == 1:
        return True

    n = len(items) - 1
    monotonic_increasing = True
    while n > 1:
        if not items[n] >= items[n-1]:
            monotonic_increasing = False
        n -= 1

    n = len(items) - 1
    monotonic_decreasing = True
    while n > 1:
        if not items[n] <= items[n-1]:
            monotonic_decreasing = False
        n -= 1

    return monotonic_decreasing or monotonic_increasing


if __name__ == '__main__':
    print(sum_array([1, 2, 3, 4, 0, 9]))
    print(find_largest([0, 4, 2, 6, 9, 7, 5]))
    print(reverse_list([0, 4, 2, 6, 9, 7, 5]))
    print(rotate_list([0, 4, 2, 6, 9, 7, 5], 3))
    print(split_and_concat([0, 4, 2, 6, 9, 7, 5], 4))
    print(remainder_array_multiplication([1, 4, 2, 7, 5], 3))
    print(is_monotonic([5, 15, 20, 10]))
