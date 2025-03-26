## **1. Villkor i programmering (If-satser)**  

### **Vad är villkor?**  
Villkor används i programmering för att styra vilka delar av koden som ska köras beroende på vissa regler. I Python används `if`, `elif` och `else` för att skapa villkor.

### **Exempel 1: Enkla villkor**
```python
x = int(input("Ange ett nummer: "))

if x > 0:
    print("Talet är positivt")
elif x < 0:
    print("Talet är negativt")
else:
    print("Talet är noll")
```

### **Exempel 2: Villkor med flera uttryck**
```python
ålder = int(input("Ange din ålder: "))

if ålder >= 18 and ålder < 65:
    print("Du är vuxen.")
elif ålder >= 65:
    print("Du är pensionär.")
else:
    print("Du är minderårig.")
```

### **Övningar**
1. Skriv ett program som frågar efter en persons kroppstemperatur och avgör om personen har hypotermi (< 35°C), normal temperatur (35-37.5°C) eller feber (> 37.5°C).
2. Skapa ett program där användaren matar in två tal, och programmet avgör vilket som är störst.
3. Skriv en meny där användaren väljer en maträtt och programmet svarar vilka ingredienser som behövs.



## **2. Loopar i programmering**

### **Vad är loopar?**  
Loopar används för att upprepa kod flera gånger utan att behöva skriva samma kod om och om igen.

### **For-loop**
```python
for i in range(1, 6):
    print(f"Iteration nummer {i}")
```

### **While-loop**
```python
x = 0
while x < 5:
    print(f"x är {x}")
    x += 1
```

### **Övningar**
1. Skapa en for-loop som skriver ut alla jämna tal mellan 1 och 20.
2. Skriv en gissningslek där programmet väljer ett slumpmässigt nummer mellan 1 och 10, och användaren gissar tills de får rätt.
3. Skapa en while-loop som ber användaren mata in ett namn, och avslutas när de skriver "exit".



## **3. Listor och Tuples**  

### **Vad är listor och tuples?**  
- Listor används för att lagra flera värden i en ordnad sekvens. 
- Tuples fungerar likadant men kan inte ändras efter att de har skapats.

### **Exempel: Lista**
```python
frukter = ["äpple", "banan", "apelsin"]
frukter.append("druva")  # Lägger till ett element
print(frukter[1])  # Output: banan
```

### **Exempel: Tuple**
```python
färger = ("röd", "grön", "blå")
print(färger[0])  # Output: röd
```

### **Övningar**
1. Skapa en lista över dina fem favoritfilmer och skriv ut dem med en for-loop.
2. Skapa en tuple med tre bilmärken och försök ändra ett av dem. Vad händer?
3. Gör en lista där användaren kan lägga till och ta bort objekt interaktivt.



## **4. Dictionaries och Sets**  

### **Vad är dictionaries och sets?**  
- Dictionaries lagrar nyckel-värdepar (exempelvis namn och ålder).
- Sets är en samling unika värden.

### **Exempel: Dictionary**
```python
person = {"namn": "Alice", "ålder": 25}
print(person["namn"])  # Output: Alice
person["stad"] = "Stockholm"
```

### **Exempel: Set**
```python
unika_tal = {1, 2, 3, 3, 4}
print(unika_tal)  # Output: {1, 2, 3, 4} (dubbletter försvinner)
```

### **Övningar**
1. Skapa en dictionary där nyckeln är en persons namn och värdet är deras favoritfärg.
2. Skapa två sets och hitta gemensamma element med `.intersection()`.



## **5. Funktioner i Python**  

### **Vad är funktioner?**  
Funktioner gör att vi kan återanvända kod och hålla våra program organiserade.

### **Exempel**
```python
def addera(a, b):
    return a + b

resultat = addera(5, 3)
print(resultat)  # Output: 8
```

### **Övningar**
1. Skriv en funktion som räknar antalet vokaler i en sträng.
2. Skapa en funktion som kontrollerar om ett tal är udda eller jämnt.



## **6. Felhantering**  

### **Vad är felhantering?**  
Fel kan hanteras med `try-except`.

### **Exempel**
```python
try:
    tal = int(input("Ange ett tal: "))
    print(10 / tal)
except ZeroDivisionError:
    print("Du kan inte dividera med noll!")
except ValueError:
    print("Ange ett giltigt heltal!")
```

### **Övningar**
1. Försök att hämta ett index i en lista som inte finns, och hantera felet.
2. Skapa ett program där användaren matar in en text istället för en siffra, och hantera felet.



## **7. Återanvändbar och modulär kod**  

### **Vad är moduler?**  
Man kan importera funktioner från andra filer.

### **Exempel: Skapa en modul**  
Fil: `minmodul.py`  
```python
def kvadrat(x):
    return x * x
```

Huvudprogrammet:  
```python
import minmodul
print(minmodul.kvadrat(4))  # Output: 16
```

### **Övningar**
1. Skapa en modul som innehåller en funktion som beräknar area av en cirkel.
2. Importera en inbyggd modul, som `math`, och använd `math.sqrt()`.

### **Utmaning**  
Skriv ett program där användaren kan:  
1. Ange namn och ålder  
2. Få ett välkomstmeddelande beroende på ålder  
3. Få sitt favoritnummer upphöjt till 2 med en funktion  
4. Se felmeddelanden om de matar in ogiltiga värden  

