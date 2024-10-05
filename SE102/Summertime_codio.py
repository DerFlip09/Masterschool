def get_user_number():
    user_number = int(input("Enter your number: "))
    return user_number


def main():
    '''this is the main function'''
    user_number = 0
    while user_number < 1000:
        user_number += get_user_number()
    print(f"Final sum: {user_number}")


if __name__ == "__main__":
    main()

############################# MASTERSCHOOL SOLUTION #######################
# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-03-22 06:31:29
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-03-22 06:39:06

"""
Summer Time

- Asks the user to input numbers in a loop
- Calculate continuously the sum of all the numbers typed
- When the sum reaches 1000 (or more), the loop will stop
and the final sum will be printed
- No need to check the validity of the input
- Assume the user always input integers
"""
SUM_LIMIT = 1000


def main():
    """
    Main function
    """
    total = 0
    while total < SUM_LIMIT:
        total += int(input("Please enter a number: "))
    print(f"Final sum: {total}")


if __name__ == "__main__":
    main()
