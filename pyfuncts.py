import math

def ispalindrome(string):
    return string == string[::-1]

# function returning factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


# function returning primes from a defined range
def primes(n):
    x = []
    for i in range(2, n + 1):
        g = math.floor(i ** (1 / 2))
        s = 0
        for j in range(1, g + 1):
            if i % j == 0:
                s += 1
        if s == 1:
            x .append(i)
    return x


def factors(n):
    x = []
    for i in range(2, n):
        if n % i == 0:
            x.append(i)
    return x


def product(x):
    s = 1
    for i in range(0, len(x)):
        s *= x[i]
    return s


if __name__ == '__main__':
    pass
#     # print(g)
#     if g =='int' or g == 'float':
#         print(n*5)
#     elif g == 'str':
#         print(n)
