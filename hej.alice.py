# Importera datetime för att hämta aktuellt år
from datetime import datetime

# Fråga efter namn och ålder
namn = input("Vad heter du? ")
ålder = int(input("Hur gammal är du? "))

# Hämta aktuellt år
nuvarande_år = datetime.now().year

# Justera beräkningen beroende på om användaren redan fyllt år
år_fyller_100 = nuvarande_år + (100 - ålder) - (input("Har du redan fyllt år i år? (ja/nej): ").strip().lower() == "nej")

# Skriv ut resultatet
print("Hej " , namn , ", du kommer att fylla 100 år, år " , str(år_fyller_100) , ".")