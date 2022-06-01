seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
  print("Os segmentos podem formar um tranigulo")
  if seg1 == seg2 and seg2 == seg3:
    print("O triangulo é EQUILÁTERO")
  elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
    print("O triangulo é ESCALENO")
  else:
    print("O triangulo é ISÓCELES")
else: 
  print("Os segmentos acima não podem formar um triangulo")
