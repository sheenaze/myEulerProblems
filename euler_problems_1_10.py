import math
from pyfuncts import *


# 1st problem ==============================================
def problem_1(n=1000):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


# print(problem_1())

# 2nd problem ==============================================

def problem_2(maximum_value=4 * (10 ** 6)):
    x = [1, 2]
    while x[-1] + x[-2] < maximum_value:
        x = x + [x[-1] + x[-2]]
    s = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            s += x[i]
    return s


# print(problem_2())

# 3rd problem ==============================================
n = 600851475143


def problem_3(number=600851475143):
    fsqr = math.floor(math.sqrt(number))
    x = []
    y = []
    for i in range(2, fsqr + 1):
        if n % i == 0:
            x.append(i)
    for i in range(0, len(x)):
        z = math.floor(math.sqrt(x[i]))
        s = 0
        for j in range(1, z + 1):
            if x[i] % j == 0:
                s += 1
        if s == 1:
            y = y + [x[i]]
    return y


# print(problem_3())

# 4th problem  ====================================================================
def problem_4(number_of_digit=3):
    x = []
    start_range = 10 ** (number_of_digit - 1)
    end_range = 10 ** number_of_digit
    for i in range(start_range, end_range):
        for j in range(start_range, end_range):
            number = i * j
            number_str = str(number)
            if ispalindrome(number_str):
                x.append(number)
    return max(x)


# print(problem_4())


# 5th problem ==============================================
def problem_5(max_factor = 20):
    real_factors = []
    for i in range(1, max_factor + 1):
        if isprime(i):
            real_factors.append(i)
        elif product(real_factors) % i != 0:
            i_primes = prime_factors(i)
            real_factors += [element for element in i_primes if product(real_factors) * element % i == 0]
    return product(real_factors)

#
# print(problem_5())


# 6th problem ==============================================
def problem_6(number=100):
    s = sum([i ** 2 for i in range(1, number + 1)])
    sq_s = sum([i for i in range(1, number + 1)]) ** 2
    return abs(s - sq_s)


# print(problem_6())

# 7th problem ==============================================
def problem_7(max_num=10001):
    prime_numbers = []
    i = 2
    while len(prime_numbers) < max_num:
        g = int(i ** (1 / 2))
        s = 0
        for k in range(1, g + 1):
            if i % k == 0:
                s += 1
        if s == 1:
            prime_numbers.append(i)
        i += 1
    return prime_numbers[-1]


# print(problem_7())

#  8th problem ==============================================
def problem_8(num=13):
    numb = '''73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586
    156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445
    231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713
    810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475
    224352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137
    565705605749026140797296865241453510047482166370484403199890008895243450658541227588666881164271714799244429282308
    634656748139191231628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506
    941658960408071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071760605
    88611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'''
    numb_list = list("".join(numb.split()))
    numb_list_int = [int(h) for h in numb_list]
    prod = []
    bord = len(numb_list_int) - len(numb_list_int) % num
    for i in range(0, bord - num):
        p = numb_list_int[i]
        for j in range(i + 1, i + num):
            p *= numb_list_int[j]
        prod.append(p)
    return max(prod)


# print(problem_8())

#  9th problem ==============================================
def problem9(sum_abc=1000):

    '''function returns three numbers fullfilling relations:
    a+b+c = sum_abc and a**2 + b**2 = c**2'''

    sqb = int((sum_abc ** 2) / 2)
    abc = []
    for i in range(1, sqb + 1):
        if int(i ** (1 / 2)) % (i ** (1 / 2)) == 0:
            abc.append(int(i ** (1 / 2)))
    for a in abc[0:-3]:
        for b in abc[1:-2]:
            for c in abc[2:-1]:
                if a + b + c == sum_abc and a ** 2 + b ** 2 == c ** 2:
                    print([a, b, c])
                    return a * b * c
    return


# print(problem9(1000))

#  10th problem ==============================================
# problem 10
def problem_10(maximum_prime = 2*10**6):
    return sum(primes(maximum_prime))

# print(problem_10())


