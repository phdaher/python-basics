from random import randint 
print("Olá, eu sou seu computador...")
print("Acabei de pensar em número entre 0 e 10.")
print("Será que você consegue advinhar qual foi?")
user = int(input("Qual é seu palpite? "))
computer  = randint(0, 10)
tentativas = 1
while user != computer:
  if computer > user:
    user = int(input("Mais... Tente mais uma vez: "))
  else:
    user = int(input("Menos... Tente mais uma vez: "))
  tentativas += 1
print("Você acertou com {} tentativas".format(tentativas))