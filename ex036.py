casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o salario do comprador? "))
financiamento = float(input("Com quantos anos de fincanciamento? "))
if (casa / (financiamento * 12) > salario * 0.3):
  print("O emprestimo não pode ser aprovado")
else:
  print("O emprestimo vai ser aprovado")
