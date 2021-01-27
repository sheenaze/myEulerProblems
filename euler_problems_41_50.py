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

