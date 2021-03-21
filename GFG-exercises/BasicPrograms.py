import math


def addition(a, b):
    return a + b


def max_num(a, b):
    if a > b:
        return a
    else:
        return b


def factorial(n):
    if n < 0:
        return 0
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product


def simple_interest(principle_amount, time, rate):
    return (principle_amount*time*rate)/100


def compound_interest(principle_amount, time, rate):
    amount = principle_amount * (1 + rate/100) ** time
    return amount - principle_amount


def armstrong(n):
    if n < 0:
        return "not positive"
    digits = str(n)
    length = len(digits)
    i = 0
    summation = 0
    while i < length:
        summation += int(digits[i]) ** len(digits)
        i += 1
    return summation == n


def circle_area(radius):
    return radius**2 * math.pi


def prime_numbers(start, end):
    numbers = list(range(2, end+1))
    primes = []
    i = 0
    while i < len(numbers):
        primes.append(numbers[i])
        j = i+1
        while j < len(numbers):
            if numbers[j] % numbers[i] == 0:
                numbers.pop(j)
            else:
                j += 1
        i += 1

    i = 0
    while i < len(primes):
        if primes[i] < start:
            primes.pop(i)
        else:
            i += 1

    return primes


def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def nth_fibonacci(n):
    if n <= 0:
        return "number must be a positive number"
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib1 = 0
    fib2 = 1
    i = 2
    while i < n:
        fib2 = fib2 + fib1
        fib1 = fib2 - fib1
        i += 1
    return fib2


def nth_multiple_in_fibonacci(k, n):
    if k == 0:
        return "0 does not have any multiples"
    count = 0
    i = 1
    fib1 = 0
    fib2 = 1
    while count < n:
        fib2 = fib2 + fib1
        fib1 = fib2 - fib1
        if fib2 % k == 0:
            count += 1
        i += 1
    return i


def get_ascii(character):
    return ord(character)


def sum_of_squares(n):
    if n <= 0:
        return 0
    return n**2 + sum_of_squares(n-1)


def sum_of_cubes(n):
    summed = 0
    while n > 0:
        summed += n**3
        n = n - 1
    return summed


if __name__ == '__main__':
    print(addition(1, 2))
    print(max_num(1, 2))
    print(factorial(-1))
    print(simple_interest(10000, 5, 5))
    print(compound_interest(10000, 10.25, 5))
    print(armstrong(1253))
    print(circle_area(2))
    print(prime_numbers(1, 33))
    print(is_prime(17))
    print(nth_fibonacci(12))
    print(nth_multiple_in_fibonacci(4, 5))
    print(get_ascii('a'))
    print(sum_of_squares(4))
    print(sum_of_cubes(7))
