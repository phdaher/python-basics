total = 0
numero = int(input("Digite um numero: "))
for i in range(1, numero + 1):
  if numero % i == 0:
    print('\033[33m', end=" ")
    total += 1
  else:
    print('\033[31m', end=" ")
  print('{}'.format(i), end=" ")
print("O numero {} foi divisivel {} vezes".format(numero, total))

if total == 2:
  print("O número É primo")
else:
  print("O número NÃO É primo")
