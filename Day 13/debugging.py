# program 13.1 Describe Problem
def my_function():
    for i in range(1, 20):
        # answer: for i in rang(1,20+1)
        if i == 20:
            print("You got it")


my_function()

# program 13.2  Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# answer: dice num = randint(0, 5)
print(dice_imgs[dice_num])

# program 13.3 Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
# answer :if year >= 1980:
    if year <= 1994:
        print("You are a millennial.")
    elif year > 1994:
        print("You are a Gen Z.")

# program 13.4 Fix the Errors
age = input("How old are you?: ") # int should be inserted to value the statement
if age >= 18:
    print("You can drive at age {age}.") # add f-string to fix this line

# # program 13.5 Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # remove one = sign
# add this statement print(f"Pages = {pages},\n word = {word_per_page} ")
total_words = pages * word_per_page
print(total_words)

# program 13.6 Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)
#  indent the program to print the values

mutate([1, 2, 3, 5, 8, 13])

# program 13.7 debugging odd and even
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
# answer indent the program and modify like 2 == 0 to get output

# program 13.8 debugging leap year
year = input("Which year do you want to check?: ")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
# answer : add int in input statement

# program 13. 9 debugging fizzbuzz
for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:  # use and operator instead of or
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # rewrite as print(number)
