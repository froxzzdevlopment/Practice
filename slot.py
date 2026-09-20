import random

s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
s2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
s3 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

z= 0

while True:
    a = random.choice(s1)
    b = random.choice(s2)
    c = random.choice(s3)
    d = (a, b, c)
    z+=1
    if d == (7, 7, 7) and z >= 1:
        print(d)
        print(z)
        break