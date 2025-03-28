# Skapa en lista
min_lista = [10, 20, 30, 40, 50]

# Användaren får välja ett index
try:
    index = int(input("Skriv in ett index: "))
    värde = min_lista[index]
    print(f"Värdet på index {index} är {värde}.")
except IndexError:
    print(f"Index {index} finns inte i listan. Listan har bara {len(min_lista)} element.")
except ValueError:
    print("Du måste skriva in ett giltigt heltal.")