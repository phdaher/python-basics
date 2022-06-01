numero = int(input("Informe um número "))
print(f"Analisando o número {numero}")
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Unidade", u)
print("Dezena",d)
print("Centena", c)
print("Milhar", m)