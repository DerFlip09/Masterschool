
def checks_and_convert_single_digit(input):
    numbers_str = list(input)
    numbers_int = [int(numbers_str[0], 10), int(numbers_str[2], 10)]
    return numbers_int


def single_addition(input):
    numbers = checks_and_convert_single_digit(input)
    result = numbers[0] + numbers[1]
    return int(result)


def single_subtraction(input):
    numbers = checks_and_convert_single_digit(input)
    return numbers[0] - numbers[1]


def single_divison(input):
    numbers = checks_and_convert_single_digit(input)
    return numbers[0] / numbers[1]


def single_multiplication(input):
    numbers = checks_and_convert_single_digit(input)
    return numbers[0] * numbers[1]


def single_integer_division(input):
    numbers = checks_and_convert_single_digit(input)
    result = [numbers[0] // numbers[1], numbers[0] % numbers[1]]
    return f"The answer is {result[0]}\nThe remainder is {result[1]}"


def calculate(text_input):
    if "+" in text_input:
        result = single_addition(text_input)
    elif "-" in text_input:
        result = single_subtraction(text_input)
    elif "*" in text_input:
        result = single_multiplication(text_input)
    elif "~" in text_input:
        result = single_integer_division(text_input)
    else:
        result = single_divison(text_input)
    return result


def main():
    print("Welcome to the Python calculator!")
    times = int(input("How many calculations do you want to do? "))
    for i in range(times):
        user_input = input("What do you want to calculate? ")
        result = calculate(user_input)
        if type(result) == type(3) or type(result) == type(.3):
            print(f"The answer is {result}")
        else:
            print(result)


if __name__ == "__main__":
    main()

# Solution of Masterschool for this problem
OPERATORS_SUPPORTED = ("+", "-", "*", "/", "~")


def get_operator(operation):
    """
    Returns operator from given operation
    """
    for element in operation:
        if element in OPERATORS_SUPPORTED:
            return element
    return None


def calculate(operation):
    """
    Prints result of given operation
    """
    operator = get_operator(operation)

    # split operation by operator to get operands
    operands = operation.split(operator)
    first_num = int(operands[0])
    second_num = int(operands[1])
    if operator == "+":
        print(f"The answer is {first_num + second_num}")
    if operator == "-":
        print(f"The answer is {first_num - second_num}")
    if operator == "*":
        print(f"The answer is {first_num * second_num}")
    if operator == "/":
        print(f"The answer is {first_num / second_num}")
    if operator == "~":
        print(f"The answer is {first_num // second_num}")
        print(f"The remainder is {first_num % second_num}")


def main():
    """
    Main function
    """
    print("Welcome to the Python calculator!")
    nb_calculations = int(input("How many calculations do you want to do? "))
    for i in range(nb_calculations):
        given_operation = input("What do you want to calculate? ")
        calculate(given_operation)

if __name__ == "__main__":
    main()
