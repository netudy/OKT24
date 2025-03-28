# Importera math-modulen för att få tillgång till matematiska funktioner
import math

# Beräkna kvadratroten av ett tal
def berakna_kvadratrot(tal):
    """
    Beräknar kvadratroten av ett tal med hjälp av math.sqrt().
    
    Args:
        tal (float): Talet som vi vill beräkna kvadratroten av (måste vara >= 0).
        
    Returns:
        float: Kvadratroten av talet.
        
    Raises:
        ValueError: Om talet är negativt (kvadratrot ur negativa tal är inte reellt).
        
    Exempel:
        >>> berakna_kvadratrot(16)
        4.0
        
        >>> berakna_kvadratrot(-1)
        Traceback (most recent call last):
            ...
        ValueError: Talet kan inte vara negativt för reell kvadratrot.
    """
    if tal < 0:
        raise ValueError("Talet kan inte vara negativt för reell kvadratrot.")
    return math.sqrt(tal)

# Testa funktionen
print(berakna_kvadratrot(25))  # Output: 5.0
print(berakna_kvadratrot(2))   # Output: 1.4142135623730951

try:
    print(berakna_kvadratrot(-9))  # Kommer att ge ValueError
except ValueError as e:
    print(e)  # Output: "Talet kan inte vara negativt för reell kvadratrot."