from pyfuncts import *
from itertools import permutations, combinations_with_replacement


# 31st problem ==============================================
def poly(a, b, c, d, e, f, g, h):
    return a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h


def problem31():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_to_find = 200
    ways_number = 0
    file_name = 'numbers.txt'
    file = open(file_name, 'w')
    for h in range(0, 2):
        for g in range(0, 2 - 2 * h + 1):
            for f in range(0, 4 - 2 * g - 4 * h + 1):
                for e in range(0, 10 - int(2.5 * f) - 5 * g - 10 * h + 1):
                    for d in (0, 20 - 2 * e - 5 * f - 10 * g - 20 * h + 1):
                        for c in range(0, 40 - 2 * d - 4 * e - 10 * f - 20 * g - 40 * h + 1):
                            for b in range(0, 100 - int(2.5 * c) - 5 * d - 10 * e - 25 * f - 50 * g - 100 * h + 1):

                                a_max = 200 - 2 * b - 5 * c - 10 * d - 20 * e - 50 * f - 100 * g - 200 * h + 1
                            
                                for a in range(0, a_max):
                                    file.write(f'{[a, b, c, d, e, f, g, h]} \n')
                                    print(a, b, c, d, e, f, g, h)
                                    ways_number += 1 if poly(a, b, c, d, e, f, g, h) == coin_to_find else 0
    file.close()
    return ways_number


print(problem31())
