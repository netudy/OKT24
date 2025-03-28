import random  # Importera random-modulen för att generera ett slumpmässigt nummer

def gissningslek():
    # Generera ett slumpmässigt nummer mellan 1 och 10
    slumpmässigt_nummer = random.randint(1, 10)
    
    # Skapa en variabel för att hålla reda på användarens gissning
    gissning = None
    
    # Loopa tills användaren gissar rätt
    while gissning != slumpmässigt_nummer:
        # Be användaren att gissa
        gissning = int(input("Gissa ett nummer mellan 1 och 10: "))
        
        # Ge feedback till användaren
        if gissning < slumpmässigt_nummer:
            print("För lågt, försök igen!")
        elif gissning > slumpmässigt_nummer:
            print("För högt, försök igen!")
        else:
            print(f"Grattis! Du gissade rätt. Det hemliga numret var {slumpmässigt_nummer}.")

# Starta spelet
gissningslek()