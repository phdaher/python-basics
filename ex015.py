dias_alugado = float(input("Qunatos dias o carro foi alugado? ")) 
km_rodados = float(input("Quantos kilometros foram rodados? ")) 
total_pagar = (dias_alugado * 60) + (km_rodados * 0.15)
print(f"O total para pagar no aluguel é de {total_pagar}")