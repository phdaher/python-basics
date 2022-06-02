sexo = str(input("Qual é o sexo da pessoa? [M/F] ")).strip().upper()[0]
while sexo not in "MF":
  sexo = str(input("Dados inválidos, por favor informe seu sexo [M/F] ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))