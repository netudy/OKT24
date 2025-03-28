ålder = int(input("Ange din ålder: "))

if ålder >= 18 and ålder < 65:
    print("Du är vuxen.")
elif ålder >= 65:
    print("Du är pensionär.")
else:
    print("Du är minderårig.")