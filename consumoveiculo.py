carros = []
consumos = []

# Dados
for i in range(3):
    carro = input(f"Carro {i + 1}: ").strip()
    consumo = float(input("Km por litro: "))
    carros.append(carro)
    consumos.append(consumo)

print("\n" "=============================================" "\n")

# Cálculos
for i in range(3):
    litros = 500 / consumos[i]
    custo = litros * 4.90
    print(f"{carros[i]} - {consumos[i]} - {litros:.1f} litros - R$ {custo:.2f}")