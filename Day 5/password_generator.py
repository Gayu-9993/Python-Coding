print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# easy level
password = " "
new_password = " "
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(f"New Easy Level Password is: {password}")
# hard level
nr_password = len(password)
password = list(password)
random.shuffle(password)
for char in password:
    new_password += char
print(f"New Hard Level Password is: {new_password}")
