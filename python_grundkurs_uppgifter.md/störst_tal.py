# Programmet jämför två tal och berättar vilket som är störst

# Fråga användaren efter det första talet och konvertera inmatningen till ett heltal
tal1 = int(input("Skriv in ett tal: "))

# Fråga användaren efter det andra talet och konvertera inmatningen till ett heltal
tal2 = int(input("Skriv in ett till tal: "))

# Jämför de två talen
if tal1 > tal2:
    # Om tal1 är större än tal2, skriv ut detta
    print(f"{tal1} är större än {tal2}")
elif tal1 < tal2:
    # Om tal2 är större än tal1, skriv ut detta
    print(f"{tal2} är större än {tal1}")
else:
    # Om talen är lika stora, skriv ut detta
    print("Talen är lika stora")