
def sum(number_one, number_two):  # intended
    return number_one + number_two


def is_subset(subset_list, superset_list):
    is_subset_flag = True
    for item in subset_list:
        if item not in superset_list:
            is_subset_flag = False
        elif subset_list.count(item) != superset_list.count(item):
            is_subset_flag = False
    return is_subset_flag
