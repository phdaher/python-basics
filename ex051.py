print("="*30)
print("10 TERMOS DE UMA P.A")
print("="*30)
termo_1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo_n =  termo_1 + (10 - 1) * razao
for i in range(termo_1, termo_n + razao, razao):
  print(i, end=" -> ")
 