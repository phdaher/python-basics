peso = float(input("Qual é o seu peso (KG)? "))
altura = float(input("Qual é a sua altura (m)? "))
imc = peso / (altura ** 2)
if imc > 40:
  print("Obesidade morbida")
elif imc < 40 and imc >= 30:
  print("Obesidade")
elif imc < 30 and imc >= 25:
  print("Sobrepeso")
elif imc < 25 and imc >= 20:
  print("Peso ideal")
else:
  print("Abaixo do peso")