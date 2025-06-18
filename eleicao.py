votos_chapa1 = 0
votos_chapa2 = 0
votos_chapa3 = 0
votos_branco = 0
votos_nulo = 0

total_votantes = 10
eleitor = 1  # Contador de eleitores

print("Eleição - Clube Os nerds")
print("Digite o número correspondente ao seu voto:")
print("1 para Chapa 1")
print("2 para Chapa 2")
print("3 para Chapa 3")
print("4 para Voto em Branco")
print("5 para Voto Nulo")

while eleitor <= total_votantes:
    try:
        voto = int(input(f"Voto do eleitor {eleitor}: "))
        if voto == 1:
            votos_chapa1 += 1
            eleitor += 1
        elif voto == 2:
            votos_chapa2 += 1
            eleitor += 1
        elif voto == 3:
            votos_chapa3 += 1
            eleitor += 1
        elif voto == 4:
            votos_branco += 1
            eleitor += 1
        elif voto == 5:
            votos_nulo += 1
            eleitor += 1
        else:
            print("Voto inválido. Digite um número de 1 a 5.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print("\nRESULTADO DA ELEIÇÃO:")
print(f"A Chapa 1 teve {votos_chapa1} votos")
print(f"A Chapa 2 teve {votos_chapa2} votos")
print(f"A Chapa 3 teve {votos_chapa3} votos")
print(f"Total de votos em branco: {votos_branco}")
print(f"Total de votos nulos: {votos_nulo}")

# Contabilizando o primeiro turno
votos_validos = votos_chapa1 + votos_chapa2 + votos_chapa3
maior_votacao = max(votos_chapa1, votos_chapa2, votos_chapa3)

vencedor = None
if votos_chapa1 == maior_votacao and votos_chapa1 > votos_validos / 2:
    vencedor = "Chapa 1"
elif votos_chapa2 == maior_votacao and votos_chapa2 > votos_validos / 2:
    vencedor = "Chapa 2"
elif votos_chapa3 == maior_votacao and votos_chapa3 > votos_validos / 2:
    vencedor = "Chapa 3"

if vencedor:
    print(f"\n{vencedor} venceu no primeiro turno com mais de 50% dos votos válidos.")
else:
    print("\nNenhuma chapa venceu no primeiro turno, a eleição terá um próximo turno.")
