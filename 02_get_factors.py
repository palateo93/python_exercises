def get_two_factors(num_list, result):
    temp_list = set()
    for pos in range(0, len(num_list)):
        actual_value = num_list[pos]
        quotient = result / actual_value
        if quotient in temp_list:
            return quotient, actual_value
        else:
            temp_list.add(actual_value)
    return None


def get_three_factors(num_list, result):
    temp_list = set()
    for pos in range(0, len(num_list)):
        actual_value = num_list[pos]
        quotient = result / actual_value
        if get_two_factors(num_list, quotient):
            return actual_value, get_two_factors(num_list, quotient)[0], get_two_factors(num_list, quotient)[1]
    return None


numbers = [1, 5, 30, 10, -2, -5, 6, -10]

print(get_two_factors(numbers, 6))
print(get_three_factors(numbers, 200))
