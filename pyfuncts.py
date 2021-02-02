import math
import numpy as np
import time
from timeit import default_timer as timer


def ispalindrome(string):
    return string == string[::-1]


# function returning factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


# function returning primes from a defined range


def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def divisors(number):
    """
    Function for computing a number divisors, more effective than factors function (for large numbers)
    :param number: a natural number
    :return: divisors of the given number
    """
    square_root = int(math.sqrt(number))
    number_factors = [i for i in range(1, square_root + 1) if number % i == 0]
    for ind in range(0, len(number_factors)):
        div = number / number_factors[ind]
        if div not in number_factors:
            number_factors.append(div)
    return sorted(number_factors)


def product(x):
    s = 1
    for element in x:
        s *= element
    return s


def isprime(num):
    boundary  = int(num ** (1/2)) + 1
    if num == 1:
        return False
    for i in range (2, boundary):
        if num % i == 0:
            return False
    return True


def primes(n):
    return [i for i in range(2, n + 1) if isprime(i)]


def n_first_primes(n):
    primes = []
    i = 1
    while len(primes) < n:
        if isprime(i):
            primes.append(i)
        i += 1
    return primes


def prime_factors(max_num):
    num_factors = factors(max_num)
    return [number for number in num_factors if isprime(number)]


def anti_diagonal(arr):
    return np.fliplr(arr).diagonal()


def sum_to_n(n):
    return int(n * (n + 1) * 0.5)


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def sum_of_digits(number):
    number_as_list = list(str(number))
    result = 0
    for element in number_as_list:
        result += int(element)
    return result


def days_numbers(year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days[1] = 29
    return days


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
        yield a


def is_pandigital(number, first_number=1):
    num_txt = str(number)
    num = first_number
    while str(num) in num_txt:
        num += 1
    return num == len(num_txt) + first_number


def triangle_numbers(limit_number):
    triangle_numbers = [1/2 * num * (num + 1) for num in range(1, limit_number + 1)]
    return triangle_numbers


def pentagonal_numbers(limit_index):
    pent_nums = [num * (num * 3 - 1) / 2 for num in range(1, limit_index + 1)]
    return pent_nums

def is_pentagonal(num):
    n = (1 + (24 * num + 1) ** (1/2)) / 6
    return int(n) == n and n > 0

# if __name__ == '__main__':
    # start = timer()
    # for num in range(100 + 1):
    #     # print('number', num)
    #     is_prime = isprime(num)
    # end = timer()
    # print(end - start)
    # #
    # start = timer()
    # for num in range(1000 + 1):
    #     is_prime = isprime(num)
    # end = timer()
    # print(end - start)
    # #
    # start = timer()
    # for num in range(10000 + 1):
    #     is_prime = isprime(num)
    # end = timer()
    # print(end - start)
    # #
    # for num in range(100000 + 1):
    #     is_prime = isprime(num)
    # end = timer()
    # print(end - start)
    #
    # for num in range(1000000 + 1):
    #     is_prime = isprime(num)
    # end = timer()
    # print(end - start)
    #
    # start = timer()
    # print(primes(100))
    # end = timer()
    # print(end - start)
    #
    # start = timer()
    # print(primes(1000))
    # end = timer()
    # print(end - start)
    #
    # start = timer()
    # print(primes(10000))
    # end = timer()
    # print(end - start)
    #
    # start = timer()
    # print(primes(100000))
    # end = timer()
    # print(end - start)
    #
    # start = timer()
    # print(primes(1000000))
    # end = timer()
    # print(end - start)

    # print(factors(2520))

    # for i in range(10**5, 10**6):
    #     start1 = time.time()
    #     f1 = factors(i)
    #     end1 = time.time()
    #     dif1 = end1 - start1
    #
    #
    #     start2 = time.time()
    #     f2 = divisors(i)
    #     end2 = time.time()
    #     dif2 = end2 - start2
    #     if len(f1) != len(f2):
    #         # print(f1, f2)
    #         print(i, dif1, dif2, len(f1), len(f2), 'UWAGA!!!')
    #     else:
    #         print(i, round(dif1/dif2, 2) ,dif1, dif2)
