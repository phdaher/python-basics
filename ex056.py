somaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for i in range(1,5):
  print("----- PESSOA {} -----".format(i))
  nome = str(input("Nome: ")).strip()
  idade = int(input("Idade: "))
  sexo = str(input("Sexo [M/F}: ")).strip()
  somaidade = somaidade + idade
  if i == 1 and sexo in "Mm":
    maioridadehomem = idade
    nomevelho = nome
  if sexo in "Mn" and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo == "Ff" and idade > 20:
    totmulher20 += 1
print("A média de idade do grupo é de {}".format(sum(somaidade)/(i)))
print("O homem mais velho tem {} e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20)) 