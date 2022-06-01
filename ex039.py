from datetime import date
nasc = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - nasc

print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18:
  print("Você deve se alistar imediatamente")
elif idade < 18:
  print("Ainda faltam {} anos pro alistamento".format(18 - idade))
  print("Seu alistamento será em {}".format(atual + (18 - idade)))
else:
  print("Você passou {} aos da idade de alistar".format(atual - (nasc +18)))