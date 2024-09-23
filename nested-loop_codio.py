def is_odd(num):
    return num % 2 != 0


def print_upper_triangle(num):
    """
    Prints an upper triangle pattern of numbers.

    :param num: The height of the triangle.
    """
    for triangle_range in range(1, num + 1):
        for num in range(1, triangle_range + 1):
            print(num, end="")
        print()


def print_lower_triangle(num):
    """
    Prints a lower triangle pattern of numbers.

    :param num: The height of the triangle.
    """
    for triangle_range in range(num, 0, -1):
        for num in range(1, triangle_range):
            print(num, end="")
        print()


def print_triangle(n):
    """
    Prints an upper and lower triangle pattern.

    :param n: The height of the triangles.
    """
    print_upper_triangle(n)
    print_lower_triangle(n)


def print_multiplication_header(num):
    """
    Prints the header for a multiplication table.

    :param num: The size of the multiplication table.
    """
    print("  ", end="")
    for number in range(1, num + 1):
        print(f"{number:3}", end="")
    print()


def print_multiplication_body(num):
    """
    Prints the body of a multiplication table.

    :param num: The size of the multiplication table.
    """
    for number in range(1, num + 1):
        print(f"{number:2}", end="")
        for multiplier in range(1, num + 1):
            print(f"{number * multiplier:3}", end="")
        print()


def print_multiplication_table(num):
    """
    Prints a complete multiplication table.

    :param num: The size of the multiplication table.
    """
    print_multiplication_header(num)
    print_multiplication_body(num)


COMMAND_LIST = {
    "triangle": print_triangle,
    "mp": print_multiplication_table
}


def main():
    """
    Main function to execute user commands for printing triangles or multiplication tables.

    :raises ValueError: If the input is not a positive number.
    :raises KeyError: If the command is not recognized.
    """
    while True:
        try:
            number = int(input("Please enter a number: "))
        except ValueError:
            print("Please enter a positive number")
            continue
        if number < 0:
            print("Bye!")
            break
        command = input("Please enter command (triangle/mp): ")
        if not is_odd(number) and command == "triangle":
            print("Number must be odd for triangle!")
            continue
        elif command not in COMMAND_LIST.keys():
            print("Command does not exists!")
            continue
        else:
            COMMAND_LIST[command](number)


if __name__ == "__main__":
    main()
