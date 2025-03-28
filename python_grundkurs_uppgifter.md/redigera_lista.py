# Skapa en tom lista
min_lista = []

# Huvudloop för programmet
while True:
    # Visa menyn för användaren
    print("\nVad vill du göra?")
    print("1. Visa listan")
    print("2. Lägg till ett objekt")
    print("3. Ta bort ett objekt")
    print("4. Avsluta programmet")
    
    
    # Be användaren välja ett alternativ
    val = input("Ange ditt val (1-4): ")
    
    # Hantera användarens val
    if val == "1":
        # Visa listan
        if min_lista:  # Kontrollera om listan inte är tom
            print("\nDin lista:")
            for index, objekt in enumerate(min_lista, start=1):
                print(f"{index}. {objekt}")
        else:
            print("\nListan är tom.")
    
    elif val == "2":
        # Lägg till ett objekt
        nytt_objekt = input("\nAnge ett objekt att lägga till: ")
        min_lista.append(nytt_objekt)
        print(f"'{nytt_objekt}' har lagts till i listan.")
    
    elif val == "3":
        # Ta bort ett objekt
        if min_lista:  # Kontrollera om listan inte är tom
            print("\nDin lista:")
            for index, objekt in enumerate(min_lista, start=1):
                print(f"{index}. {objekt}")
            try:
                index = int(input("Ange numret på objektet du vill ta bort: ")) - 1
                if 0 <= index < len(min_lista):
                    borttaget_objekt = min_lista.pop(index)
                    print(f"'{borttaget_objekt}' har tagits bort från listan.")
                else:
                    print("Ogiltigt nummer. Försök igen.")
            except ValueError:
                print("Ogiltig inmatning. Ange ett nummer.")
        else:
            print("\nListan är tom. Inget att ta bort.")
    
    elif val == "4":
        # Avsluta programmet
        print("\nProgrammet avslutas. Hej då!")
        break
    
    else:
        # Ogiltigt val
        print("\nOgiltigt val. Försök igen.")