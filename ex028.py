import random
print('Vou pensar em número entre 0 e 5')
print('PROCESSSANDO...')
numero = str(input('Em que número eu pensei? '))
n = random.randint(0, 5)
if (numero == n):
  print("Acertou")
else:
  print("Errou")