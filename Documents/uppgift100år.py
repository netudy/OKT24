from datetime import datetime

# Hämta dagens datum
nuvarande_år = datetime.now().year
nuvarande_månad = datetime.now().month
nuvarande_dag = datetime.now().day

# Fråga efter användarens namn och ålder
namn = input("Vad heter du? ")
ålder = int(input("Hur gammal är du? "))
födelsemånad = int(input("Vilken månad är du född? (1-12) "))
födelsedag = int(input("Vilken dag är du född? (1-31) "))

# Beräkna året då användaren fyller 100
år_fyller_100 = nuvarande_år + (100 - ålder)

# Om användaren inte haft sin födelsedag ännu i år, justera beräkningen
if (födelsemånad > nuvarande_månad) or (födelsemånad == nuvarande_månad and födelsedag > nuvarande_dag):
    år_fyller_100 -= 1

# Skriv ut resultatet
print(f"Hej {namn}, du kommer att fylla 100 år, år {år_fyller_100}.")