from pyfuncts import *
from itertools import combinations_with_replacement


# def problem_51():
#     n = 5
#     minimum = min_n_digit_number(n)
#     maximum = max_n_digit_number(n)
#     prime_list = primes_in_range(minimum, maximum)
#     print(prime_list)
#     print(len(prime_list))
#

# problem_51()

# def problem_52():
#     nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
#     cond = True
#     length = 3
#     all_numbers = []
#     combs = [int(''.join(comb)) for comb in combinations_with_replacement(nums, 3)]
#     print(combs)
#     i = 0
#     while cond and i < len(combs):
#         for comb in combs:
#             if len(str(comb)) == length and 3/2 * comb in combs and 2 * comb in combs and 5/2 * comb in combs and 3 * comb in combs:
#                 print(comb)
#                 cond = False
#             i += 1

# problem_52()


def problem_53():
    vals = []
    for n in range(1, 101):
        for r in range(1, n+1):
            val = factorial(n) / (factorial(r) * factorial(n-r))
            if val > 10 ** 6:
                vals.append(val)
    return vals

# print(len(problem_53()))


