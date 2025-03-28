def räkna_volkaler(sträng):

	vokaler = "aeiouyåäöAEIOUYÅÄÖ"

	antal_volkaler = sum(1 for tecken in sträng if tecken in vokaler)

	return antal_volkaler

användbar_text = input("Skriv in en text: ")


resultat = räkna_volkaler(användbar_text)

print(f"Antal vokaler i din text: {resultat}")