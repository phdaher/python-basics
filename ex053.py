frase = str(input("Digite aqui uma frase: ")).upper().replace(" ", "")
frase_invertida = frase[::-1]
print(frase, frase_invertida)
if frase == frase_invertida:
  print("A frase digitada é um palindro")
else:
  print("A frase digitada não é um palindro")