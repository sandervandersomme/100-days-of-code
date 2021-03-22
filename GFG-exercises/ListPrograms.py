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


def clear_list(items):
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


if __name__ == '__main__':
    print(swap_first_last_element([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(swap_elements([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0], 4, 6))
    print(find_length([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(is_present([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0], 1))
    print(clear_list([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(reverse_list([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0]))
    print(multiply_elements([3,4,5]))
    print(second_largest([3,4,5]))
    print(n_largest([6, 7, 8, 4, 3, 2, 5, 6, 7, 9, 0], 3))

