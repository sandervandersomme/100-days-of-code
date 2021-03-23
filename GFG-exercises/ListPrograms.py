from functools import reduce


def swap_first_last_element(items):
    new_list = items
    new_list.append(items[0])
    new_list[0] = new_list.pop(-2)
    return new_list


def swap_elements(items, pos1, pos2):
    new_list = items
    new_list[pos1], new_list[pos2] = new_list[pos2], new_list[pos1]
    return new_list


def find_length(items):
    return len(items)


def is_present(items, element):
    return element in items


def clear_list():
    return []


def reverse_list(items):
    items.reverse()
    return items


def multiply_elements(items):
    return reduce((lambda item1, item2: item1 * item2), items)


def second_largest(items):
    items.remove(max(items))
    return max(items)


def n_largest(items, n):
    return sorted(items)[-n:]


def even_numbers(items):
    n = len(items)
    while n - 1 >= 0:
        if items[n - 1] % 2 != 0:
            del items[n - 1]
        n = n - 1
    return items


def odd_numbers(items):
    n = len(items)
    while n - 1 >= 0:
        if items[n - 1] % 2 == 0:
            del items[n - 1]
        n -= 1
    return items


def even_in_range(start, end):
    return list(filter(lambda x: (x % 2 == 0), list(range(start, end))))


def odd_in_range(start, end):
    return [x for x in list(range(start, end)) if (x % 2 != 0)]


def positive_numbers(items):
    return [x for x in items if (x % 2 != 0)]


def negative_numbers(items):
    return list(filter(lambda x: (x >= 0), items))


def count_element(items, element):
    return items.count(element)


def remove_empty_tuples(tuples):
    return list(filter(None, tuples))


if __name__ == '__main__':
    print(swap_first_last_element([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(swap_elements([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0], 4, 6))
    print(find_length([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(is_present([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0], 1))
    print(clear_list())
    print(reverse_list([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(multiply_elements([3, 4, 5]))
    print(second_largest([3, 4, 5]))
    print(n_largest([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0], 3))
    print(even_numbers([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(odd_numbers([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(even_in_range(2, 8))
    print(odd_in_range(2, 8))
    print(count_element([2, 4, 5, 8, 8, 7, 9, 8], 8))
    print(remove_empty_tuples([(), (), (2, 4), (2, 5), ()]))


