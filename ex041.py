from datetime import date
ano = date.today().year 
nasc = int(input("Informe sua data de nasc: "))
idade = ano - nasc
print(idade)
if idade > 25:
  print("Master")
elif idade > 19 and idade < 25:
  print("Senior")
elif idade > 14 and idade < 19:
  print("Junior")
elif idade > 9 and idade < 14:
  print("Infantil")
else:
  print("Mirim")