import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
size = nr_letters + nr_symbols + nr_numbers
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for n in range(0, nr_letters):
    password += random.choice(letters)

for n in range(0, nr_numbers):
    password += random.choice(numbers)
for n in range(0, nr_symbols):
    password += random.choice(symbols)

print(password)
print(len(password))
randompassword = []

for n in range(0, nr_letters):
    randompassword.append(random.choice(letters))

for n in range(0, nr_numbers):
    randompassword.append(random.choice(numbers))
for n in range(0, nr_symbols):
    randompassword.append(random.choice(symbols))

random.shuffle(randompassword)

strpass = ""
for n in randompassword:
    strpass += n
print(strpass)
print(len(strpass))
