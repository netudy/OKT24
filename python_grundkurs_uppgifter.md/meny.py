# Funktion som visar ingredienser beroende på vald maträtt
def visa_ingredienser(vald_matratt):
    if vald_matratt == 1:
        print("Ingredienser för Spaghetti Carbonara:")
        print("Spaghetti, ägg, bacon, parmesan, svartpeppar")
    elif vald_matratt == 2:
        print("Ingredienser för Tacos:")
        print("Tortillabröd, köttfärs, tacokrydda, ost, sallad, tomat, gräddfil")
    elif vald_matratt == 3:
        print("Ingredienser för Kycklinggryta:")
        print("Kyckling, lök, morötter, grädde, vitlök, buljongtärning")
    elif vald_matratt == 4:
        print("Ingredienser för Grönsakspaj:")
        print("Pajdeg, broccoli, paprika, ost, ägg, grädde")
    else:
        print("Ogiltigt val, vänligen välj en korrekt maträtt.")

# Meny
def huvudmeny():
    while True:  # Låt användaren försöka tills de gör ett giltigt val
        print("Välj en maträtt:")
        print("1. Spaghetti Carbonara")
        print("2. Tacos")
        print("3. Kycklinggryta")
        print("4. Grönsakspaj")
        
        try:
            val = int(input("Ange nummer på maträtten: "))
            if val in [1, 2, 3, 4]:  # Kolla om valet är giltigt
                visa_ingredienser(val)
                break  # Bryt ut ur loopen när ett giltigt val görs
            else:
                print("Ogiltigt val, vänligen välj ett nummer mellan 1 och 4.")
        except ValueError:
            print("Vänligen skriv in ett giltigt nummer.")

# Starta programmet
huvudmeny()
