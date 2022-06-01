import random
from time import sleep
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("=-"*30)
computador = random.randint(0, 2)
itens = ["Pedra", "Papel", "Tesoura"]

if jogador == computador:
  print("Empatou, você jogou {} e o computador jogou {}". format(itens[jogador], itens[computador]))
if jogador == 0 and computador == 1:
  print("O computador ganhou, você jogou {} e o computador jogou {}". format(itens[jogador], itens[computador]))
if jogador == 0 and computador == 2:
  print("Você ganhou, você jogou {} e o computador jogou {}". format(itens[jogador], itens[computador]))
if jogador == 1 and computador == 0:
  print("Você ganhou, você jogou {} e o computador jogou {}". format(itens[jogador], itens[computador]))
if jogador == 1 and computador == 2:
  print("O computador ganhou, você jogou {} e o computador jogou {}". format(itens[jogador], itens[computador]))
