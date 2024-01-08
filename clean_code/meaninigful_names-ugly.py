def sum(number_one, number_two):
    return number_one + number_two

def is_subset(list_one, list_two):
    is_subset_flag = True
    for item in list_one:
        if item not in list_two:
          is_subset_flag = False
    return is_subset_flag