lista = []
for i in range(1, 6):
  peso = float(input("Peso da pessoa {}: ".format(i)))
  lista.append(peso)
print(lista)
print("O maior peso entre as pessoas é: {}".format(max(lista)))
print("O menor peso entre as pessoaas é: {}".format(min(lista)))