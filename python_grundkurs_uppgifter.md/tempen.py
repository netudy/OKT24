# Uppgift: Temperatur

# Fråga användaren om deras kroppstemperatur och konvertera inmatningen till ett decimaltal
temp = float(input("Vad har du för kroppstemperatur? "))

# Kontrollera temperaturen och ge feedback baserat på värdet
if temp < 35:
    # Om temperaturen är under 35 grader, har personen hypotermi
    print("Du har hypotermi.")
elif 35 <= temp <= 37.5:
    # Om temperaturen är mellan 35 och 37.5 grader, är det en normal kroppstemperatur
    print("Du har normal kroppstemperatur.")
else:
    # Om temperaturen är över 37.5 grader, har personen feber
    print("Du har feber.")