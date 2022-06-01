print("="*30)
preco = float(input("Preço das compras: R$:"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
pagamento = int(input("Qual vai ser o meio de pagamento? "))
if pagamento == 1:
  preco = preco * 0.9
  print(f"O preço com o desconto do pagamento a vista vai ser {preco}")
if pagamento == 2:
  preco = preco * 0.95
  print(f"O preço com o desconto do pagamento a vista no cartao vai ser {preco}")
if pagamento == 3:
  print(f"O preço em 2x cartao vai ser {preco}")
if pagamento == 4:
  preco = preco * 1.2
  print(f"O preço em 3x ou mais no cartão vai ser de {preco}")