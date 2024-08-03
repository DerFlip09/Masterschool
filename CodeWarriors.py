# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase)
# and numeric digits.

'''def duplicate_count(text):
    sum_duplicates = 0
    test_text = text.lower()
    test_chars = set(test_text)
    for i in test_chars:
        char_count = test_text.count(i)
        if char_count > 1:
            sum_duplicates = sum_duplicates + 1
        else:
            pass
    return sum_duplicates'''

# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

'''def find_it(seq):
    test_seq = set(seq)
    for num in test_seq:
        num_count = seq.count(num)
        if num_count % 2 == 0:
            pass
        else:
            return num'''


def filter_list(list_of_strings_and_nums):
    'return a new list with the strings filtered out'
    return [char for char in list_of_strings_and_nums if type(char) is int]


print(filter_list([4, 5, "h"]))
