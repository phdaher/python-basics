velocidade = int(input("Qual a velocidade do carro? "))
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print(f"Você passou dos limites e deverá pagar uma multa de {multa} reais")
else:
  print("Continue dirigindo com segurança")
