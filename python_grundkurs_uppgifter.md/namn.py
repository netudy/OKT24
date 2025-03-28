# Initiera variabeln 'namn' med värdet None
namn = None

# Starta en while-loop som fortsätter så länge 'namn' inte är lika med "exit"
while namn != "exit":
    # Be användaren mata in ett namn eller skriva "exit" för att avsluta programmet
    namn = input("Skriv in ett namn eller skriv exit för att avsluta Programmet: ")
    
    # Kontrollera om användaren har skrivit "exit" (oavsett stor/liten bokstav)
    if namn.lower() == "exit":
        # Meddela användaren att programmet avslutas
        print("Programmet avslutas.")
        # Avbryt loopen och avsluta programmet
        break
    
    # Om användaren inte skrev "exit", skriv ut det inmatade namnet
    print(f"Du har skrivit {namn}, skriv ett till namn eller skriv exit för att avsluta Programmet.")