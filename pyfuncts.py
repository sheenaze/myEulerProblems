import math
import numpy as np
import time


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
    factors_below_root = [i for i in range(1, square_root + 1) if number % i == 0]
    factors_above_root = []
    for i in range(1, len(factors_below_root) - 1):
        for j in range(i, len(factors_below_root)):
            element = factors_below_root[i] * factors_below_root[j]
            if element not in factors_below_root and number % element == 0:
                factors_below_root.append(element)
    factors_below_root.extend(factors_above_root)
    return factors_below_root


def product(x):
    s = 1
    for element in x:
        s *= element
    return s


def isprime(num):
    return len(factors(num)) == 2


def primes(n):
    return [i for i in range(2, n + 1) if isprime(i)]


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


if __name__ == '__main__':
    print(factors(2520))

    start1 = time.time()
    f1 = factors(60*10**6)
    print(len(f1), f1)
    end1 = time.time()
    dif1 = end1 - start1

    start2 = time.time()
    f2 = divisors(60*10**6)
    print(len(f2), f2)
    end2 = time.time()
    dif2 = end2 - start2

    print(dif1, dif2)
