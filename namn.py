# While-loop för att mata in namn tills "exit" skrivs
while True:
    namn = input("Skriv ett namn (eller skriv 'exit' för att avsluta): ")
    if namn.lower() == "exit":
        print("Programmet avslutas.")
        break
    else:
        print(f"Du skrev: {namn}")
