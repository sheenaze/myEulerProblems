from pyfuncts import *
from itertools import permutations, combinations_with_replacement
import numpy as np
import statistics
from timeit import default_timer as timer

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

# 32nd problem ==============================================
def problem32():
    min_multiplicand = 2
    max_multiplicand = 98
    min_multiplier = 123
    max_multiplier = 4987
    excluded_multiplicands = [num for num in range(min_multiplicand, max_multiplicand+1) if len(set(str(num))) != len(str(num))]
    excluded_multipliers = [num for num in range(min_multiplier, max_multiplier+1) if len(set(str(num))) != len(str(num))]

    results = []
    for multiplicand in range(min_multiplicand, max_multiplicand + 1):
        for multiplier in range(min_multiplier, max_multiplier + 1):
            if multiplier not in excluded_multipliers and multiplicand not in excluded_multiplicands:
                val = multiplicand * multiplier
                txt = str(val) + str(multiplicand) + str(multiplier)
                if ''.join(sorted(txt)) == '123456789' and val not in results:
                    print()
                    results.append(val)
    # print(results)
    return sum(results)

# print(problem32())

# 33rd problem ==============================================
def problem33():
    min_num = 11
    max_num = 98
    min_den = 12
    max_denom = 99
    excluded = [num for num in range(min_num, max_denom+1) if num%10 == 0]

    prod = 1
    for num in range(min_num, max_num+1):
        for denom in range(num+1, max_denom+1):
            num_txt = sorted(str(num))
            den_txt = sorted(str(denom))
            repeated = [num in den_txt for num in num_txt]
            if any(repeated) and num not in excluded and denom not in excluded:
                # print('old', num, denom)
                ind = repeated.index(True)
                ind_den = den_txt.index(num_txt[ind])
                num_txt.pop(ind)
                new_num = int(num_txt[0])
                den_txt.pop(ind_den)
                new_den = int(den_txt[0])
                frac = num / denom
                frac_new = new_num / new_den
                # print('new', new_num, new_den)
                if frac == frac_new:
                    prod *= frac
                    # print({num:denom})
                    # print({new_num: new_den})

    return(prod)
# print(problem33())

# 34th problem ==============================================
def problem34():
    num_dict ={
        0: 1,
        1: factorial(1),
        2: factorial(2),
        3: factorial(3),
        4: factorial(4),
        5: factorial(5),
        6: factorial(6),
        7: factorial(7),
        8: factorial(8),
        9: factorial(9),
    }
# print(num_dict)

# 35th problem ==============================================


def problem35(num):
    primes_to_num = primes(num)
    primes_str = []
    for prime in primes_to_num:
        ps = str(prime)
        cond = '0' not in ps and '2' not in ps and '4' not in ps and '5' not in ps and '6' not in ps and '8' not in ps
        if cond or len(ps) == 1:
            primes_str.append(ps)
    circulars = []
    for prime in primes_str:
        if len(np.unique(list(prime))) == 1:
            circulars.append([prime])
        else:
            rots_for_prime = [prime]
            for perm in permutations(prime):
                new_val = ''.join(perm)
                while new_val != prime and new_val in primes_str:
                    rots_for_prime.append(new_val)
                    primes_str.remove(new_val)
            if len(rots_for_prime) == len(prime):
                circulars.append(rots_for_prime)
    return sum([len(item) for item in circulars])


# print(problem35(1000000))


# 36th problem ==============================================


def problem36(limit):
    result = 0
    for num in range(limit + 1):
        if ispalindrome(str(num)):
            num_2 = bin(num).split('b')[1]
            if ispalindrome(num_2):
                result += num
    return result

# limit = 10 ** 6
# print(problem36(limit))

# 37th problem ==============================================
def problem37():
    num = 10
    truncatables = []
    while len(truncatables) != 11:
        num += 1
        if isprime(num):
            nls1 = list(str(num))
            cond2 = all([str(val) not in str(num) for val in [0, 4, 6, 8]])
            if cond2:
                nls2 = list(str(num))
                ls = len(str(num))
                i = 0
                while len(nls1) > 1:
                    nls1.pop(-1)
                    new_num = int(''.join(nls1))
                    i += 1 if isprime(new_num) else 0
                if ls-1 == i:
                    i = 0
                    while len(nls2) > 1:
                        nls2.pop(0)
                        new_num = int(''.join(nls2))
                        i += 1 if isprime(new_num) else 0
                if ls-1 == i:
                    print('Hurray!', num)
                    truncatables.append(num)
    return(sum(truncatables))

# print(problem37())

# 38th problem ==============================================
# 39th problem ==============================================


def problem39(p_max):
    perimeters = []
    for a in range(1, int(p / 2)):
        for b in range(a, p):
            c = (a ** 2 + b ** 2) ** (1/2)
            if int(c) == c and sum([a, b, c]) <= p:
                perimeters.append(sum([a,b,c]))

    return statistics.mode(perimeters)
#
# p = 1000
# print(problem39(p))