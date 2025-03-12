import datetime

# Fråga användaren om namn och ålder
namn = input("Vad heter du? ")
ålder = int(input("Hur gammal är du? "))

# Fråga om användaren har fyllt år i år
har_fyllt_ar = input("Har du fyllt år i år? (ja/nej) ").strip().lower()

# Hämta nuvarande år
nuvarande_ar = datetime.datetime.now().year

# Beräkna födelseår
fodelse_ar = nuvarande_ar - ålder
if har_fyllt_ar == "nej":
    fodelse_ar -= 1  # Justera om användaren inte har fyllt år än

# Beräkna vilket år personen fyller 100
hundra_ars_ar = fodelse_ar + 100

# Skriv ut resultatet
print(f"Hej {namn}, du kommer att fylla 100 år, år {hundra_ars_ar}.")