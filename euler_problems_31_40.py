from pyfuncts import *
from itertools import permutations, combinations_with_replacement
import numpy as np

# 31st problem ==============================================
def problem31_inefficient():
    coins = np.array([1, 2, 5, 10, 20, 50, 100, 200])
    coin_to_find = coins[-1]
    nums = 0
    for a in range(0, coin_to_find // 1 + 1):
        for b in range(0, coin_to_find // 2 + 1):
            for c in range(0, coin_to_find // 5 + 1):
                for d in range(0, coin_to_find // 10 + 1):
                    for e in range(0, coin_to_find // 20 + 1):
                        for f in range(0, coin_to_find // 50 + 1):
                            for g in range(0, coin_to_find // 100 + 1):
                                for h in range(0, coin_to_find // 200 + 1):
                                    coeffs = np.array([a, b, c, d, e, f, g, h])
                                    result = np.matmul(coeffs, coins)
                                    if result == coin_to_find:
                                        nums += 1
                                        print(nums)
    print(nums)

def problem31_efficient(nums, max_num):
    ways = [0] * (max_num + 1)
    ways[0] = 1
    for x in nums:
        for i in range(x, max_num+1):
            ways[i] += ways[i-x]
    print(ways)
    return ways[-1]

nums = [1,2,5,10,20,50,100,200]
# print(problem31_efficient(nums, max(nums)))
