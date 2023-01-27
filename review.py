numero = int(input('Digite um numero: '))
ePrimo = 0
for i in range(1, (numero + 1)):
  if numero % i == 0:
    ePrimo += 1
if ePrimo == 2:
  print('É primo')
else:
  print('Não é primo')