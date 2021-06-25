from pyfuncts import *
from itertools import permutations, combinations_with_replacement, combinations
import math
import numpy as np
import statistics
from timeit import default_timer as timer

# 41st problem ==============================================


def problem41():
    nums = list('123456789')
    cond = False
    while len(nums) >= 1 and not cond:
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
            cond = int(''.join(perm[i:i + 3])) % primes[i - 1] == 0
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

# 45th problem ==============================================
def problem45():
    # not efficient way
    num = 40756
    cond = is_hexagonal(num) and is_pentagonal(num) and is_triangle(num)
    while not cond:
        num += 1
        cond = is_hexagonal(num) and is_pentagonal(num) and is_triangle(num)
    return num


#
# print(problem45())

# 46th problem ==============================================
def append_primes(primes_list, new_border):
    for number in range(primes_list[-1], new_border - 1):
        if isprime(number):
            primes_list.insert(0, number)
    return primes_list


def append_double_squares(list_of_ds, new_border):
    for number in range(list_of_ds[-1], new_border):
        res = (number / 2) ** (1/2)
        if int(res) == res:
            list_of_ds.insert(0, number)
    return list_of_ds


def check_the_number_based_on_primes(number, primes_list):
    for prime in primes_list:
        result = number - prime
        res = (result / 2) ** (1 / 2)
        if int(res) == res:
            return True
    print('And the winner is: ', number)
    return False


def check_the_number_based_on_ds(number, list_of_ds):
    for ds in list_of_ds:
        result = number - ds
        if isprime(result):
            return True
    print('The winner is: ', number)
    return False


def problem_46_based_on_primes():
    primes_list = [7, 5, 3, 2]
    number = 9
    cond = True
    while cond:
        if not isprime(number):
            primes_list = append_primes(primes_list, number)
            cond = check_the_number_based_on_primes(number, primes_list)
        number += 2


def problem_46_based_on_ds():
    ds_list = [8, 2]
    number = 9
    cond = True
    while cond:
        if not isprime(number):
            ds_list = append_double_squares(ds_list, number)
            cond = check_the_number_based_on_ds(number, ds_list)
        number += 2


# problem_46_based_on_primes() # result after around 191 seconds
# problem_46_based_on_ds() # result after around 4 seconds

def problem_47():
    # a working solution, but not efficient one
    numb = 4
    primes_list = primes(700)
    prod_list = []
    for comb in combinations(primes_list, numb):
        num_prod = math.prod(comb)
        prod_list.append(num_prod)
        for num in comb:
            prod_list.append(num * num_prod)
    sorted_list = sorted(prod_list)
    sorted_list.insert(0, sorted_list[0])
    d = np.diff(sorted_list)
    ind0 = 0
    cond = True
    while cond:
        if sum(d[ind0:ind0+numb-1]) == numb-1:
            print(ind0, sorted_list[ind0:ind0+numb], d[ind0:ind0+numb-1], sum(d[ind0:ind0+numb-1]))
            cond = False
        ind0 += 1


# problem_47()

def problem_48():
    result = 0
    for i in range(1, 1001):
        result += i ** i
    res_char = str(result)
    print(res_char[-10:])


# problem_48()

def problem_49():
    numbers = ['0', '1', '2','3', '4', '5', '6', '7', '8', '9']
    for comb in combinations_with_replacement(numbers, 4):
        list_of_numbs = []
        for perm in permutations(comb):
            if perm[0] != '0':
                joined = int(''.join(perm))
                if isprime(joined) and joined not in list_of_numbs:
                    list_of_numbs.append(joined)
        abs_diffs = abs_differences_between_all_elements(list_of_numbs)
        if len(list_of_numbs) >= 3 and check_how_many_times_repeats(3330, abs_diffs) == 2:
            print(list_of_numbs, (abs_differences_between_all_elements(list_of_numbs)))


# problem_49()