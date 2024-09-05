#############1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num =num + 1


################2
inches = 0
while inches >= 0:
    inches = int(input("Enter the number of inches to be converted to cm: "))
    centimeters = inches * 2.54
    if inches < 0:
        print("exit")
    else:
        print(f"{inches} inches is equal to {centimeters} cm")

##################3
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    numbers.append(int(user_input))

if numbers:
    smallest = largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print("Smallest number:", smallest)
    print("Largest number:", largest)


################4
import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < number:
        print("its too low!")
    elif guess > number:
        print("its too high!")
    else:
        print("Correct!")
        break

############5
correctusername="python"
correctpass= "rules"
attempts = 0
while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correctusername and password == correctpass:
        print(f"Welcome {username}")
        break
    else:
        attempts = attempts + 1
    if attempts == 5:
        print("Access denied! The correct username is python and password is rules")

###########6
import random
def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            inside_circle = inside_circle + 1

    pi_approximation = 4 * inside_circle / num_points
    return pi_approximation

num_points = int(input("Enter the number of random points to generate: "))
pi_value = estimate_pi(num_points)
print(f"Approximation of π: {pi_value}")


