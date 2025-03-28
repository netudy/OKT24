def berakna_kvadrat(nummer):
    """Returnerar talet upphöjt till 2 (kvadraten)"""
    return nummer ** 2

def main():
    print("Välkommen till vårt program!")
    
    # Hantera namn
    while True:
        namn = input("Vad heter du? ").strip()
        if namn:  # Kontrollera att namn inte är tomt
            break
        print("Fel: Du måste ange ett namn. Försök igen!")
    
    # Hantera ålder
    while True:
        alder_input = input("Hur gammal är du? ")
        try:
            alder = int(alder_input)
            if alder < 0 or alder > 120:
                raise ValueError("Åldern måste vara mellan 0 och 120")
            break
        except ValueError:
            print("Fel: Ange en giltig ålder (heltal mellan 0 och 120). Försök igen!")
    
    # Hantera favoritnummer
    while True:
        favoritnummer_input = input("Vad är ditt favoritnummer? ")
        try:
            favoritnummer = float(favoritnummer_input)
            break
        except ValueError:
            print("Fel: Ange ett giltigt nummer. Försök igen!")
    
    # Personligt välkomstmeddelande baserat på ålder
    if alder < 18:
        print(f"\nHej {namn}! Du är ung och lovande!")
    elif 18 <= alder <= 65:
        print(f"\nHej {namn}! Du är i dina bästa år!")
    else:
        print(f"\nHej {namn}! Vishet kommer med ålder!")
    
    # Beräkna och visa kvadraten av favoritnumret
    kvadrat = berakna_kvadrat(favoritnummer)
    print(f"Ditt favoritnummer ({favoritnummer}) upphöjt till 2 är: {kvadrat}")

if __name__ == "__main__":
    main()