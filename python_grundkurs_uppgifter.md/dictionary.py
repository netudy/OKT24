# Skapa en dictionary som sparar personers favoritfärger
# Nycklarna är namn och värdena är färger
favofärg = {
    "Leon": "Svart och gult",
    "Sara": "blå",
    "Robin": "grön",
    "Elias": "röd",
    "Jem": "gul",
    "Jasin": "lila"
}

# Iterera över dictionaryn med hjälp av .items()
# .items() returnerar nyckel-värde-par som tupler
for namn, färg in favofärg.items():
    # Skriv ut en formaterad sträng som visar varje persons favoritfärg
    # {namn} ersätts med personens namn och {färg} med deras favoritfärg
    print(f"{namn}s favoritfärg är {färg}.")