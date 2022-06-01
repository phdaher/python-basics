num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para a conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTA
[ 3 ] HEXA'''
)
escolha = int(input("Digite sua opção: "))
if escolha == 1:
  print("{} convertido para  BINÁRIO é {}".format(num, bin(num)))
if escolha == 2:
  print("{} convertido para  OCTA é {}".format(num, oct(num)))
if escolha == 3:
  print("{} convertido para  HEXA é {}".format(num, hex(num)))