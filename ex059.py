n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opc = 0
while opc != 5:
  
  print('''
  [ 1 ] SOMAR
  [ 2 ] MULTIPLICAR
  [ 3 ] MAIOR
  [ 4 ] NOVOS NÚMEROS
  [ 5 ] SAIR DO PROGRAMA
  ''')
  opc = int(input("Qual é a sua opção? "))

  if opc == 1:
    print("A soma é: {}".format(n1 + n2))
    print("="*30)
  if opc == 2:
    print("A multiplicação é: {}".format(n1 * n2))
    print("="*30)
  if opc == 3:
    if n1 > n2:
      print(f"{n1} é maior número que {n2} ")
    else:
      print(f"{n1} é menor número que {n2} ")
    print("="*30)
  if opc == 4:
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
