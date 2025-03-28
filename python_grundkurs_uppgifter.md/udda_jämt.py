def udda_eller_jämnt(tal):
    # Använd modulus-operatorn (%) för att kontrollera om talet är jämnt eller udda
    if tal % 2 == 0:
        return "Jämnt"
    else:
        return "Udda"

# Exempel på användning
tal = int(input("Skriv in ett heltal: "))
resultat = udda_eller_jämnt(tal)
print(f"Talet {tal} är {resultat}.")