import math
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
#hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2))**0.5
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")