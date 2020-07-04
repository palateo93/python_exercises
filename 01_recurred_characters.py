def first_recurring_char(given_string):
    counts = dict()
    for char in given_string:
        if char in counts:
            return char
        else:
            counts[char] = 1
    return None


def first_non_recurring_char(given_string):
    counts = dict()
    min_index = len(given_string)
    first_no_occ = None

    for index, value in enumerate(given_string):
        if value in counts:
            counts[value] = (counts[value][0] + 1, counts[value][1])
        else:
            counts[value] = (1, index)
    for (char, v) in counts.items():
        if v[0] == 1 and v[1] < min_index:
            min_index = v[1]
            first_no_occ = char
    return first_no_occ


string = input("Enter the string: ")


first_recurred = first_recurring_char(string)
if first_recurred:
    print("The first recurring character is: " + first_recurred)
else:
    print("There is no recurred characters")


first_non_recurred = first_non_recurring_char(string)
if first_non_recurred:
    print("The first non recurring character is: " + first_non_recurred)
else:
    print("All characters are recurred")


# commento ste
# commento teo
