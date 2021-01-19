from pyfuncts import *
from itertools import permutations


# 21st problem ==============================================
def problem21(max_number=10000):
    amicable_numbers = []
    for number in range(1, max_number + 1):
        number_fact = divisors(number)
        first_number = sum(number_fact[0:-1])
        first_number_fact = divisors(first_number)
        second_number = sum(first_number_fact[0:-1])
        if second_number == number and second_number != first_number and second_number not in amicable_numbers:
            amicable_numbers.append(second_number)
            amicable_numbers.append(first_number)
    print(sum(amicable_numbers))


# problem21()

# 22nd problem ==============================================
def problem22(filename='names.txt'):
    file = open(filename, 'r')
    names = file.read().replace('"', '')
    names_list = sorted(names.split(','))
    i = 0
    result = 0
    for name in names_list:
        i += 1
        name_number = 0
        for letter in name:
            name_number += (ord(letter) - 64)
        score = name_number * i
        result += score
    print(result)


# problem22()

# 23rd problem ==============================================
start_number = 24
end_number = 28123  # 28123  # all integers greater than 28123 can be written as the sum of two abundant numbers


def abundant_numbers(min_number=start_number, max_number=end_number):
    abundant_numbers_set = []
    for number in range(min_number, max_number + 1):
        number_fact = divisors(number)
        number_fact_sum = sum(number_fact[0:-1])
        if number_fact_sum > number:
            # print(number, number_fact_sum)
            abundant_numbers_set.append(number)

    return abundant_numbers_set


# print(abundant_numbers())

def problem23(min_number=24, max_number=end_number):
    abundant_numbers_set = abundant_numbers(1, max_number + 1)
    non_abundant_sum = sum_to_n(23)
    for number in range(min_number, max_number):
        i = 0
        cond = True
        true_tab = []
        while abundant_numbers_set[i] < number and cond and i <= len(abundant_numbers_set):
            dif = number - abundant_numbers_set[i]
            cond = dif not in abundant_numbers_set
            true_tab.append(cond)
            print(number, cond, i)
            i += 1
        if all(true_tab):
            non_abundant_sum += number
    return non_abundant_sum


# print(problem23())


# 24th problem ==============================================
def problem24(numbers=None, permutation_index=10 ** 6):
    if numbers is None:
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permut = permutations(numbers)
    permut_list = list(permut)
    return permut_list[permutation_index - 1]


# print(problem24())


# 25th problem ==============================================
def problem25(digits=1000):
    fib = 0
    n = 1
    while len(str(fib)) < digits:
        fib_gen = fibonacci_generator(n)
        fib = list(fib_gen)[-1]
        n += 1
    return n - 1


# print(problem25())


# 26th problem ==============================================
def fractionToDecimal(numr, denr):
    res = ""
    mp = {}
    rem = numr % denr
    while ((rem != 0) and (rem not in mp)):
        # Store this remainder
        mp[rem] = len(res)
        # Multiply remainder with 10
        rem = rem * 10
        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)

        # Update remainder
        rem = rem % denr

    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]


def problem26(max_denumerator=1000):
    denominators = [denumerator for denumerator in range(2, max_denumerator+1)]
    lens = {}
    for denominator in denominators:
        res = fractionToDecimal(1, denominator)
        lens[denominator] = len(res)
    vals = list(lens.values())
    mval = max(vals)
    position = vals.index(mval)
    print(lens)
    return list(lens.keys())[position]

print(problem26())
# Driver code


# This code is contributed by divyeshrabadiya07



# 27th problem ==============================================

def quadratic(a, b, n):
    return n ** 2 + a * n + b


def problem27():
    ab = []
    lengths = []
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            ab.append([a, b])
            while isprime(quadratic(a, b, n)):
                n += 1
            lengths.append(n + 1)
    ind_max = lengths.index(max(lengths))
    print(lengths[ind_max], ab[ind_max])
    return ab[ind_max][0] * ab[ind_max][1]


# print(problem27())

# 28th problem ==============================================
def problem28(max_size=1001):
    result = 1
    i = 0
    for number in range(3, max_size + 1, 2):
        i += 1
        result += 4 * number ** 2 - 2 * number + 2 - 8 * i

    return result


# print(problem28())


# 29th problem ==============================================
def problem29():
    terms = []
    for a in range(2, 101):
        for b in range(2, 101):
            term = a ** b
            if term not in terms:
                terms.append(term)
    return len(terms)

# print(problem29())