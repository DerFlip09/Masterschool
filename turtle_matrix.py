import turtle

START_Y = 0
START_X = 0
JOHN = turtle.Turtle()
JOHN.speed(50)


def draw_circle(radius):
    JOHN.circle(radius)


def move_to(x, y):
    JOHN.penup()
    JOHN.goto(x, y)
    JOHN.pendown()


def get_matrix_and_circle():
    radius = int(input("Type in the radius: "))
    rows = int(input("How many rows? "))
    columns = int(input("How many columns? "))
    step_size = radius * 2
    end_y = START_Y - step_size * rows
    end_x = START_X + step_size * columns
    return radius, rows, columns, end_y, end_x, step_size


def main():
    radius, rows, columns, end_y, end_x, step_size = get_matrix_and_circle()
    for row in range(START_Y, end_y, -step_size):
        for column in range(START_X, end_x, step_size):
            move_to(column, row)
            draw_circle(radius)


if __name__ == "__main__":
    main()
    turtle.done()