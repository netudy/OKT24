import math

def berakna_area(radie):
    """
    Beräknar arean av en cirkel med given radie.
    
    Args:
        radie (float): Cirkelns radie (måste vara >= 0).
        
    Returns:
        float: Cirkelns area.
        
    Raises:
        ValueError: Om radie är negativ.
    """
    if radie < 0:
        raise ValueError("Radien kan inte vara negativ.")
    return math.pi * radie ** 2