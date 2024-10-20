'''def funny_sequence(number):
    return [
        "FizzBuzz" if num % 15 == 0 else
        "Fizz" if num % 3 == 0 else
        "Buzz" if num % 5 == 0 else
        num
        for num in range(1, number + 1)
    ]
print(funny_sequence(15))'''

'''import turtle
john = turtle.Turtle()
colors = ["red","orange", "yellow", "green", "blue", "purple"]
john.speed(100)
def draw_triangle():
  john.forward(80)
  john.right(120)
  john.forward(80)
  john.right(120)
  john.forward(80)
  john.right(120)
  john.forward(80)

def draw_hexagon():
  for color in colors:
    john.pensize(6)
    john.pencolor(color)
    draw_triangle()
    john.right(60)

for i in range(6):
  draw_hexagon()
  john.right(60)
  john.forward(160)'''

'''import turtle
t = turtle.Turtle()
sizes = [20, 40, 60, 80]
t.pensize(5)

def draw_square(size):
  for i in range(4):
    t.forward(size)
    t.right(90)

for size in sizes:
  draw_square(size)
  t.left(135)
  t.penup()
  t.forward(15)
  t.pendown()
  t.right(135)'''

'''import turtle
t = turtle.Turtle()
sizes = [20, 40, 60, 80]
t.pensize(5)

def draw_hexagon(size):
  for i in range(6):
    t.forward(size)
    t.right(60)

for size in sizes:
  draw_hexagon(size)
  t.left(120)
  t.penup()
  t.forward(20)
  t.pendown()
  t.right(120)'''

'''import turtle
t = turtle.Turtle()
sizes = [20, 40, 60, 80]
t.pensize(2)

def draw_square(size, fill):
  t.begin_fill()
  t.fillcolor(fill)
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.end_fill()
    

draw_square(50, "red")
'''

'''import turtle
t = turtle.Turtle()
sizes = [20, 40, 60, 80]
squares = [(30, "red"), (60, "blue"), (90, "green")]
t.pensize(2)

def draw_square(size, fill):
  t.begin_fill()
  t.fillcolor(fill)
  for i in range(4):
    t.forward(size)
    t.left(90)
  t.end_fill()
    

for size, color in squares:
  draw_square(size, color)
  t.forward(size)
'''
'''import math
list1 = [2, 4, 9, 1002, 5, 5, 7, 2, 123]
list2 = [2, 2, 2, 2, 2]

def get_max(list1):
    return max(list1)

def unique_only(list1):
    return list(set(list1))

def starts_with(word1, prefex):
    return word1.startswith(prefex)

def factorial(num1):
    return math.factorial(num1)

def all_equal(list1):
    return len(set(list1)) == 1



print(get_max(list1))
print(unique_only(list1))
print(starts_with("My Name is", "My"))
print(factorial(6))
print(all_equal(list2))
'''
'''import datetime
lee_birthdate = datetime.datetime(2001, 7, 4)
date_today = datetime.datetime.now()

years = date_today.year - lee_birthdate.year
months = date_today.month - lee_birthdate.month
days = date_today.day - lee_birthdate.day
hours = date_today.hour - lee_birthdate.hour

print(years)
print(months)
print(days)
print(hours)
print(date_today)
print(lee_birthdate)'''

'''
def get_price_and_received_amount():
    price = int(input("How much costs? "))
    amount_customer = int(input("How much is received? "))
    return price, amount_customer


def calculate_taxes(price, VAT = 11.5):
    taxed_price = price * (1+VAT/100)
    return taxed_price


def calculate_change(taxed_price, received_amount):
    return received_amount - taxed_price

def main():
    price, received_amount = get_price_and_received_amount()
    taxed_price = calculate_taxes(price)
    change = calculate_change(taxed_price, received_amount)
    print(change)


if __name__ == "__main__":
    main()
'''
'''for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()'''
'''
def list1_in_list2(lst1, lst2):
    """
    This function checks if all the items of lst1 are in lst2.
    """
    # Go over all of lst1 items
    counter1 = 0
    found = False
    while counter1 < len(lst1):
        # Search the lst1[counter1] in lst2
        counter2 = 0
        while counter2 < len(lst2):
            if lst1[counter1] == lst2[counter2]:
                found = True
            else:
                found = False
            counter2 += 1
        counter1 += 1
    # If we didn't find, we have a number in lst1 which is not in lst2
    if not found:
        return False
    # If we got here, we found all lst1 items in lst2
    return True


print(list1_in_list2([3, 2, 1], [3, 2, 6, 5, 1]))  # should be True
print(list1_in_list2([3, 2, 1], [3, 2, 6, 5]))  # should be False'''
'''
DATA = {
  "latest_from_star_wars": [
    {
      "position_on_page": 5,
      "title": "Virtual Premiere | The Mandalorian | Disney+",
      "link": "https://www.youtube.com/watch?v=1qq4Q5n3-nU",
      "channel": {
        "name": "Star Wars",
        "link": "https://www.youtube.com/user/starwars",
        "verified": "true",
        "thumbnail": "https://yt3.ggpht.com/a-/AOh14GgskYzAhYn9cvahFlka1ODJVVGGvbJA4AGorw=s68-c-k-c0x00ffffff-no-rj-mo"
      },
      "published_date": "9 hours ago",
      "views": 57855,
      "length": "29:56",
      "description": "The Mandalorian and the Child continue their journey, facing enemies and rallying allies as they make their way through a ...",
      "extensions": [
        "New"
      ],
      "thumbnail": {
        "static": "https://i.ytimg.com/vi/1qq4Q5n3-nU/hqdefault.jpg?sqp=-oaymwEZCOADEI4CSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCwGKt1H-KNnzAuF_u2C5mfiNGmbg",
        "rich": "https://i.ytimg.com/an_webp/1qq4Q5n3-nU/mqdefault_6s.webp?du=3000&sqp=CIWD9fwF&rs=AOn4CLD82MG25RdVFBTESXsHxrC8jSVYvg"
      }
    },
    {
      "position_on_page": 6,
      "title": "The Mandalorian Virtual Red Carpet Premiere, What Scares the Jedi, and More!",
      "link": "https://www.youtube.com/watch?v=dTR7q_0_YOQ",
      "channel": {
        "name": "Star Wars",
        "link": "https://www.youtube.com/user/starwars",
        "verified": "true",
        "thumbnail": "https://yt3.ggpht.com/a-/AOh14GgskYzAhYn9cvahFlka1ODJVVGGvbJA4AGorw=s68-c-k-c0x00ffffff-no-rj-mo"
      },
      "published_date": "1 day ago",
      "views": 30410,
      "length": "3:30",
      "description": "This week, in Star Wars we announce The Mandalorian Season Two virtual red carpet premiere event, find out what scares the ...",
      "extensions": [
        "New",
        "CC"
      ],
      "thumbnail": {
        "static": "https://i.ytimg.com/vi/dTR7q_0_YOQ/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCq4INL160YpyYcyCmPUgXFMAPVhQ",
        "rich": "https://i.ytimg.com/an_webp/dTR7q_0_YOQ/mqdefault_6s.webp?du=3000&sqp=CLCl9fwF&rs=AOn4CLD0LznG9CI33NgPdTE_HXahIu4dJw"
      }
    },
    {
      "position_on_page": "hidden",
      "title": "The Star Wars Show Halloween Scaretacular!",
      "link": "https://www.youtube.com/watch?v=EgpAsPYvRy0",
      "channel": {
        "name": "Star Wars",
        "link": "https://www.youtube.com/user/starwars",
        "verified": "true",
        "thumbnail": "https://yt3.ggpht.com/a-/AOh14GgskYzAhYn9cvahFlka1ODJVVGGvbJA4AGorw=s68-c-k-c0x00ffffff-no-rj-mo"
      },
      "published_date": "2 days ago",
      "views": 38469,
      "length": "11:37",
      "description": "This month on The Star Wars Show, we take a look back at The Mandalorian Season One, check out a brand new Star Wars: ...",
      "extensions": [
        "New"
      ],
      "thumbnail": {
        "static": "https://i.ytimg.com/vi/EgpAsPYvRy0/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLApJy8y6W9Hx90Ymdup5jrX_nXU8Q",
        "rich": "https://i.ytimg.com/an_webp/EgpAsPYvRy0/mqdefault_6s.webp?du=3000&sqp=CPee9fwF&rs=AOn4CLDd5RMlqSc3Wfp3jIWllwEyDU8FnQ"
      }
    }
  ]
}



def main():
  for update in DATA["latest_from_star_wars"]:
    print(f"{update["title"]} ({update["length"]})")



if __name__ == "__main__":
  main()'''

'''def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    rotated_matrix = []
    len_matrix = len(matrix)
    len_row = len(matrix[0])
    for place in range(len_row):
        new_row = []
        for row in range(len_matrix - 1, -1, -1):
            new_row.append(matrix[row][place])
        rotated_matrix.append(new_row)
    return rotated_matrix
'''

'''import plotly.express as px
import pandas as pd

# Example data
data = {
    'Ship': ['Ship1', 'Ship2', 'Ship3'],
    'Country': ['Country1', 'Country2', 'Country3'],
    'Longitude': [10.0, 20.0, 30.0],
    'Latitude': [50.0, 40.0, 30.0]
}

df = pd.DataFrame(data)

# Create the map plot
fig = px.scatter_geo(df,
                     lon='Longitude',
                     lat='Latitude',
                     hover_name='Ship',
                     hover_data={'Country': True},
                     title='Ship Locations')

# Show the plot
fig.show()'''

# parameter: List, number
# return: True or False
# task: check the sum of two consecutive numbers in list if the sum is the number
'''def check_sum_of_numbers(numbers, sum_number):
    for index in range(len(numbers) - 1):
        sum_numbers = numbers[index] + numbers[index + 1]
        if sum_numbers == sum_number:
            return True
    return False


def check_sum_of_numbers(numbers, sum_number):
    return any(numbers[i] + numbers[i + 1] == sum_number for i in range(len(numbers) - 1))


lst = [34, 34, 19]
num = 53
print(check_sum_of_numbers(lst, num))'''

'''def main():
    print("Welcome to MessageRepeatr™ - easily repeat messages!")
    filename = input("Please enter the name of file in which the messages should be written: ")
    try:
        file = open(filename, "r+")
    except FileNotFoundError:
        print(f"This file {filename} doesn't exist.")
        file = open(filename, "w")
    else:
        print("Current content of file (will be overwritten!):\n")
        print(file.read())
    message = input("\nPlease enter the message you wish to repeat: ")
    try:
        repeats = int(input("Please enter the amount of times you wish to repeat the message: "))
    except ValueError:
        print("Positive number is needed.")
    else:
        file.write(message * repeats)
        print("Successfully wrote messages to file! Goodbye 👋")
    finally:
        file.close()


main()'''

'''import requests


REQUEST_URL = "https://www.themealdb.com/api/json/v1/1/search.php?s="

def main():
    meal_name = input("Enter meal name: ")
    meal_data = requests.get(REQUEST_URL + meal_name).json()
    meal_count = len(meal_data["meals"])
    print(f"We found {meal_count} meal:\n")
    for meal in meal_data["meals"]:
        print(5*"*" + meal["strMeal"] + 5*"*")
        print(f"Category: {meal["strCategory"]}")
        print(f"Area: {meal["strArea"]}")
        print(f"Intructions:\n{meal["strInstructions"]}")



if __name__ == "__main__":
    main()'''


'''from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return """<html><body>
        <h1>Hello, world!</h1>
        The time is """ + str(datetime.now()) + """.
        </body></html>"""


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=True)'''


'''# List of dictionaries: Each dictionary represents additional information about a student.
student_info = [
    {"name": "Alice", "age": 18, "gender": "female"},
    {"name": "Bob", "age": 17, "gender": "male"},
    {"name": "Charlie", "age": 18, "gender": "male"}
]

# List of lists: Each inner list represents the grades of a student.
student_grades = [
    [85, 90, 88],
    [75, 80, 82],
    [92, 95, 89]
]

# Dictionary of dictionaries: Each inner dictionary represents additional information about a student.
student_details = {
    "Alice": {"city": "New York", "grade_level": "Senior"},
    "Bob": {"city": "Los Angeles", "grade_level": "Junior"},
    "Charlie": {"city": "Chicago", "grade_level": "Senior"}
}


# Your task is to write a Python program to perform the following tasks:
#
# 1. Calculate the average grade for each student.
# 2. Print out the name, age, grade level, and average grade for each student.
# ### Which city is the student with the highest grade average from?
#
# - Write code that works for newer sets of students as well, not just this set.
# - First focus on finding their name.

def calc_avg(grades: list):
    avg_grade = sum(grades) / len(grades)
    return avg_grade


def print_student_info(index):
    name = student_info[index].get("name")
    age = student_info[index].get("age")
    grade_level = student_details[name].get("grade_level")
    avg_grade = calc_avg(student_grades[index])
    print(f"Student: {name}\nAge: {age}\nGrade Level: {grade_level}\nAverage Grade: {avg_grade:.2f}\n")


def find_best_average_student():
    highest_avg = 0
    index = -1
    for grades in student_grades:
        avg = calc_avg(grades)
        if avg > highest_avg:
            highest_avg = avg
        index += 1
    return highest_avg, index


def main():
    for i in range(len(student_info)):
        print_student_info(i)

    grade, index = find_best_average_student()
    name = student_info[index]["name"]
    print(f"{name} from {student_details[name]["city"]} got the highest grade with {grade:.2f}")


if __name__ == "__main__":
    main()'''
'''

def number_from_list_of_digits(list_of_digits):
    """
    This function gets a list of int digits, like [1, 4, 0]
    And returns the number made out of the digits, as int (140).
	If there is a problem with input values, raises a ValueError.
	If there is a problem with input types, raises a TypeError.
    """

    if not isinstance(list_of_digits, list):
        raise TypeError("Give me a list, damn it!")
    for num in list_of_digits:
        if not isinstance(num, int):
            raise ValueError("Common give a list of NUMBERS, idgit!")
        if not 0 <= num <= 9:
            raise ValueError("Give me a list with numbers in range 0 - 9!")

    result = 0
    power = len(list_of_digits) - 1
    for number in list_of_digits:
        result += number * 10 ** power
        power -= 1
    return result

import pytest

def test_number_from_list_of_digits():
    assert number_from_list_of_digits([1, 4, 0]) == 140

def test_fail_type_number_from_list_of_digits():
    with pytest.raises(TypeError):
        number_from_list_of_digits(140)

def test_fail_value_number_from_list_of_digits():
    with pytest.raises(ValueError):
        number_from_list_of_digits([1, '4', 0])

def test_tuple_input():
    with pytest.raises(TypeError):
        number_from_list_of_digits((1, 2, 5, 6))

def test_great_numbers():
    with pytest.raises(ValueError):
        number_from_list_of_digits([100, 100500, 678, 5, 2345])

def test_negative_numbers():
    with pytest.raises(ValueError):
        number_from_list_of_digits([-1, -8, 9, 5, -6])

def test_0_first():
    assert number_from_list_of_digits([0, 9, 9]) == 99

def test_all_0():
    assert number_from_list_of_digits([0, 0, 0]) == 0


pytest.main()
'''

from SE104.flask_training.flask_app import users

print(users)