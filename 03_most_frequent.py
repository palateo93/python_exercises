def most_frequent(given_list):
    max_item = None
    max_count = -1
    temp_dict = dict()
    for num in given_list:
        if num in temp_dict:
            temp_dict[num] += 1
        else:
            temp_dict[num] = 1
        if temp_dict[num] > max_count:
            max_count = temp_dict[num]
            max_item = num
    return max_item

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

print(most_frequent(list1))
