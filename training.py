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

import primeNumber_codio
p = primeNumber_codio
number = 100
for i in range(2, number + 1):
    if p.is_prime(i) and number - i >= 2:
        for j in range(2, 1 + number - i):
            if p.is_prime(j) and j + i == number and j >= i:
                print(f"{number} is sum of {i} and {j}")
