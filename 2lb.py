import random

ABC = "АВСЕНІКМОРТХ"
first = ''
second = ''
probil = ' '
number = ''

for i in range(5):
    first = random.choice(ABC)
    second = random.choice(ABC)
    x = random.randint(1000, 9999)
    cifr = str(x)
    number = first + second + probil + cifr
    print(number)

