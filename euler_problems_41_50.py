from pyfuncts import *
from itertools import permutations, combinations_with_replacement
import numpy as np
import statistics
from timeit import default_timer as timer

# 41st problem ==============================================


def problem41():
    nums = list('123456789')
    cond = False
    while len(nums)>=1 and not cond:
            for per in permutations(nums):
                new_num = int(''.join(per))
                if isprime(new_num):
                    cond = True
            nums.pop(-1)
    return new_num

# print(problem41())

# 42nd problem ==============================================
def problem42():
    words = open("words.txt", "r")
    words_list = words.read().split(',')
    tnums = triangle_numbers(20)
    is_triangle = 0
    for word in words_list:
        num_sum = 0
        for letter in word:
            if letter != '"':
                num_sum += ord(letter) - 64
        if num_sum in tnums:
            is_triangle += 1

    return is_triangle

# print(problem42())

# 43rd problem ==============================================


def problem43():
    base_num = '1234567890'
    perms = permutations(base_num)
    max_num = 7
    primes = n_first_primes(max_num)
    result = 0
    for perm in perms:
        num = int(''.join(perm))
        i = 1
        cond = True
        while i <= max_num and cond:
            cond = int(''.join(perm[i:i+3])) % primes[i-1] == 0
            i += 1
        if i == max_num + 1 and cond:
            result += num
    return result


# print(problem43())


# 44th problem ==============================================
def problem44():
    limit = 5000
    diffs = []
    for i in range(1, limit):
        Pi = i * (i * 3 - 1) / 2
        for j in range(i + 1, limit + 1):
            Pj = j * (j * 3 - 1) / 2
            result = Pi + Pj
            diff = Pj - Pi
            if is_pentagonal(diff) and is_pentagonal(result):
                diffs.append(diff)

    return min(diffs)


# print(problem44())


