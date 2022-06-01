price = float(input("Qual é o preço do produto? R$"))
discount = 5
price_discounted = price * (1 - discount/100)
print(f"O produto que custava {price}, na promoção com desconto de {discount} vai custar {price_discounted}")