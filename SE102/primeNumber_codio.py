'''import math


def is_divisible_by(number, by):
    return number % by == 0


def is_prime(number):
    for i in range(2, 1 + int(math.sqrt(number))):
        if is_divisible_by(number, i):
            return False
    return True


def primes_in_range(start, end):
    if start > end:
        print("The start is greater than the end, please try again")
        return None
    for i in range(start, end + 1):
        if is_prime(i):
            print(f"The number {i} is prime")


def main():
    start_of_range = int(input("Enter start range: "))
    end_of_range = int(input("Enter end range: "))
    primes_in_range(start_of_range, end_of_range)


if __name__ == "__main__":
    main()
'''
############################## MASTERSCHOOL SOLUTION #########################
# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-03-22 06:17:07
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-03-31 20:42:55
"""
Prime Minister

Finds all the prime numbers in a given range of numbers.
(not including the end range number)
"""


def is_divisible_by(number, by):
  """
    Returns True if the number is divisible by by number
    """
  return number % by == 0


def is_prime(number):
  """
    Returns True if given number is a prime number
    """
  # if the given number is not greater than 1, it is not a prime number
  if number <= 1:
    return False

  # return False if the given number is divisible by any number from
  # 2 to the square root of the given number, otherwise return True
  for i in range(2, int(number**0.5) + 1):
    if is_divisible_by(number, i):
      return False
  return True


def print_primes_in_range(start, end):
  """
    Prints all the prime numbers that are between start and end,
    not including the number end itself.
    """
  for number in range(start, end):
    if is_prime(number):
      print(f"The number {number} is prime")


def main():
  """
    Main function
    """
  start = int(input("Enter start range: "))
  end = int(input("Enter end range: "))
  print_primes_in_range(start, end)


if __name__ == "__main__":
  main()

