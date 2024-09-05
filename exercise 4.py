#############1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num =num + 1


################2
inches = int(input("Enter the number of inches to be converted to cm: "))
while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} cm")
    if inches < 0:
        print("exit")
        break
    inches = int(input("Enter the number of inches to be converted to cm: "))
##################3
max_number = None
min_number = None
number = input("Enter the numbers: ")
while number != "":
    number = float(number)
    if max_number is None or max_number < number:
        max_number = number
    if min_number is None or min_number > number:
        min_number = number
    number = input("Enter the numbers: ")

print (f"the max number is {max_number} and the min number is {min_number}")

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


