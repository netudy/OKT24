import random

# Programmet väljer ett slumpmässigt tal mellan 1 och 10
nummer = random.randint(1, 10)

# Gissningslek
while True:
    gissning = int(input("Gissa ett nummer mellan 1 och 10: "))
    if gissning < nummer:
        print("För lågt! Försök igen.")
    elif gissning > nummer:
        print("För högt! Försök igen.")
    else:
        print("Grattis! Du gissade rätt!")
        break
