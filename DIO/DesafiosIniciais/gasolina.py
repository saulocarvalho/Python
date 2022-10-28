entrada = input().split()
#carro faz 12km/l
carro = 12

tempo_hora = int(entrada[0])
velocidade_media = int(entrada[1])


litros = (tempo_hora * velocidade_media) / carro

print(f'{litros:.3f}')