soma = 0
gols = int(input('Digite o número de gols: '))
while gols != -1:
    soma += gols
    gols = int(input('Digite o número de gols: '))
print(f'O jogador fez {soma} gols na temporada!')