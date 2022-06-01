soma = 0
count = 0
for i in range(1, 7):
  num = int(input("Digite o {} valor: ".format(i)))
  if num % 2 == 0:
    soma += num
    count += 1
print("Você informou {} numeros PARES e a soma deles é de {}".format(count, soma))