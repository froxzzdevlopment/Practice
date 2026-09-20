import random

u = 2
a = 0

while True:
    computer = random.randint(1, 10)
    user = int(input("Enter a number : "))
    a += 1

    if user == computer:
        print(f"Correct computer = {computer}]\n After {a} attempt")
        break
        

    else:
        print(f"Try again \n Attempt = {a}")
