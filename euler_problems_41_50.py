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


