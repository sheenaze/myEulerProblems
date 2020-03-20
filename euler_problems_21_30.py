from pyfuncts import *


# 21st problem ==============================================
def problem21(max_number=100000):
    amicable_numbers = []
    for number in range(1, max_number + 1):
        number_fact = divisors(number)
        first_number = sum(number_fact[0:-1])
        first_number_fact = divisors(first_number)
        second_number = sum(first_number_fact[0:-1])
        if second_number == number and second_number != first_number and second_number not in amicable_numbers:
            amicable_numbers.append(second_number)
            amicable_numbers.append(first_number)
            print(number, first_number, second_number)
    print(sum(amicable_numbers))


problem21()
