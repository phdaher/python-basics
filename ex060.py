import numpy
numero = int(input("Digite um número para calucluar o seu fatorial: "))
lista = []
for i in range(numero, 0, -1):
  lista.append(i)
fact = numpy.prod(lista)
print(fact)