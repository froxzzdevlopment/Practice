import random as r

u = 10
a = 0

while True:
    a += 1
    computer = r.randint(1, 10)
    if u == computer:
        print(f"Attempt = {a}")
        break