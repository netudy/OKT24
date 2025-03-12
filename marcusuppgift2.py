# Första variabeln är vilket år personen är född, då det kan ha fyllt eller inte fyllt år i nuvarande år, så måste vi veta vilket år vi ska addeara ifrån.
born = int(input("Vilket år är du föd? "))

#Andra variabeln räknar ut vilket år dem fyller hundra. D.vs du adderar 100 till året dem är födda. x + 100 = året dem är 100, där X = året dem är född.
count = born + 100

# Tredje variabeln används för att ta reda på personens ålder, för att kunna printa ut den.
age = int(input("Hur gammal är du? "))

#Fjärde variabeln anvädns för att ta reda på hens namn, så att det kan användas i print kommandet.
name = (input("Vad heter du?"))

print ("Hej",name ,"du är",age , "År gammal, och fyller hundra år", count)
