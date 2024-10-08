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

'''def filter_list(list_of_strings_and_nums):
    'return a new list with the strings filtered out'
    return [char for char in list_of_strings_and_nums if type(char) is int]
'''
'''def spin_words(sentence):
    words = sentence.split()
    controll_words = []
    for word in words:
        if len(word) >= 5:
            controll_words.append(word[::-1])
        else:
            controll_words.append(word)
    spinned_sentence = " ".join(controll_words)
    return spinned_sentence'''

# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

'''def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    new_seconds = seconds % 60

    return f"{hours:02}:{minutes:02}:{new_seconds:02}"
'''

# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# The input will be a non-negative integer.

'''
def digital_root(n):
    root_number = str(n)
    while len(root_number) != 1:
        loop_sum = 0
        for i in range(len(root_number)):
            loop_sum += int(root_number[i])
        root_number = str(loop_sum)
    return int(root_number)


print(digital_root(12345678))
print(12345678 % 9 or 9)'''

'''def sort_array(source_array):
    odd = sorted([num for num in source_array if num % 2 != 0])

    result = []
    counter = 0

    for num in source_array:
        if num % 2 != 0:
            result.append(odd[counter])
            counter += 1
        else:
            result.append(num)
    return result

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]'''

'''def move_zeros(lst):
    zeros = [num for num in lst if num == 0]
    new_lst = []
    for num in lst:
        if num == 0:
            continue
        else:
            new_lst.append(num)
    return new_lst + zeros

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array'''

'''for i in range(1, 6):  # Rows of the table
    for j in range(1, 6):  # Columns of the table
         print(f"{i * j}\t", end="")
    print()'''
'''def multiplication_table(n):
    # Print the top header
    print("  ", end="")  # Starting space for alignment
    for i in range(1, n + 1):
        print(f"{i:3}", end="")  # Print column headers
    print()  # Newline after the header

    # Print the rows
    for i in range(1, n + 1):
        print(f"{i:2}", end="")  # Print the row header
        for j in range(1, n + 1):
            print(f"{i * j:3}", end="")  # Print the products
        print()  # Newline after each row

# Call the function with the desired size
multiplication_table(10)

def print_multiplication_header(num):
    print("  ", end="")
    for number in range(1, num + 1):
        print(f"{number:3}", end="")
    print()

def print_multiplication_body(num):
    for number in range(1, num + 1):
        print(f"{number:2}", end="")
        for multiplicator in range(1, num + 1):
            print(f"{number * multiplicator:3}", end="")
        print()

def print_multiplication_table(num):
    print_multiplication_header(num)
    print_multiplication_body(num)


print_multiplication_table(4)'''

'''def is_anagram(s, t):
    test_string = list(s)
    for char in t:
        print(char)
        test_string.remove(char)
    if not test_string:
        return True
    return False

print(is_anagram("hello", "lelho"))'''
