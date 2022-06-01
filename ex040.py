nota1 = int(input("Primera nota: "))
nota2 = int(input("Segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
  print("O aluno foi aprovado")
elif media < 7 and media >= 5:
  print("O aluno está de recuperação")
else:
  print("O aluno foi reprovado")

