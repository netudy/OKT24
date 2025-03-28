
# skapar en tuple med 3 bilmärken.
Bilmärken = ("Volvo", "BMW", "Saab")

# Försöker byta namn på det första bilmärket i tuple´n (Volvo) till Tesla.
Bilmärken[0] = "Tesla"

# Försöker mata ut det första bilmärket i tuple´n
print(Bilmärken[0]) #får error: TypeError: 'tuple' object does not support item assignment
