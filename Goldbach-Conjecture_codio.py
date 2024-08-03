def get_even_number(prompt):
    """ checks the input to be even and returns the number """
    user_input = 1
    while user_input % 2 != 0:
        try:
            user_input = int(input(prompt))
        except ValueError:
            pass
    return user_input


def is_divisible_by(number, by):
    """ checks if the number is divisible by another number """
    return number % by == 0


def is_prime(number):
    """ checks if the number is divisible by another number than itself
    alias checks if the number is a prime number """
    for i in range(2, 1 + int(number**0.5)):
        if is_divisible_by(number, i):
            return False
    return True


def get_list_of_prime_pairs(number):
    """ checks if two prime numbers are the sum of the number
    than puts the pair in a tuple and returns a list of the found pairs """
    list_of_prime_pairs = []
    for i in range(2, number):
        if is_prime(i) and number - i >= 2:
            for j in range(2, 1 + number - i):
                if is_prime(j) and j + i == number and j >= i:
                    list_of_prime_pairs.append((i, j))
    return list_of_prime_pairs


def print_pairs(list_of_pairs, number_of_sum):
    """ prints the pairs in context of the number """
    for num1, num2 in list_of_pairs:
        print(f"The number {number_of_sum} equals to the sum of {num1} and {num2}")


def main():
    """ this is the main function which calls the other ones """
    number_of_sum = get_even_number("Enter an even number: ")
    list_of_pairs = get_list_of_prime_pairs(number_of_sum)
    print_pairs(list_of_pairs, number_of_sum)


if __name__ == "__main__":
    main()
