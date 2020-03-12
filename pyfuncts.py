import math
import numpy as np


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


if __name__ == '__main__':
    print(factors(2520))
