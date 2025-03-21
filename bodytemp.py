# Fråga användaren efter kroppstemperaturen
temperatur = float(input("Ange kroppstemperatur i Celsius: "))

# Kontrollera vilken temperaturkategori personen har
if temperatur < 35:
    print("Du har hypotermi.")
elif 35 <= temperatur <= 37.5:
    print("Din temperatur är normal.")
else:
    print("Du har feber.")