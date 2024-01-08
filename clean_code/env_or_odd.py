def get_odd_numbers_from_list(numbers):
    odd_numbers = []
    for number in numbers:
        if is_odd_number(number):
            odd_numbers.append(number)
    return odd_numbers

def is_odd_number(number):
    if number % 2 != 0:
        return False
    return True
get_odd_numbers_from_list(numbers)


import random