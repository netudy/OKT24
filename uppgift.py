#På punkt a låter input användaren mata in information, i det här fallet i heltal eftersom vi använder int.
#På punkt b adderar programmet 100 år på det årtal du är född.
#Vid punkt c får användaren specificera sin ålder, åter igen via kommandot input men denna gången i vanlig text.
#På punkt d specificerar användaren sitt namn.
#Slutligen ber vi programmet skriva ut resultatet på skärmen via kommandot print.
#Användaren får en hälsning med sitt namn samt resultatet av uträkningen.

a = int(input ("Vilket år är du född? "))
b = a + 100
c = int(input("Hur gammal är du? "))
d = (input("Vad heter du? "))
print ("Hej",d ,"du är",c , "år gammal och fyller 100 år", b)