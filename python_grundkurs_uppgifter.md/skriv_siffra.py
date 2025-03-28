# Be användaren att skriva in en siffra
try:
    siffra = int(input("Skriv in en siffra: "))
    print(f"Du skrev in siffran: {siffra}")
except ValueError:
    print("Fel: Du måste skriva in en giltig siffra, inte text.")