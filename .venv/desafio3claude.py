cont = 0
soma = 0
gols = int(input('Digite o número de gols: '))
while gols != -1:
    cont += 1
    soma += gols
    gols = int(input('Digite o número de gols: '))
print(f'O jogador fez {cont} jogos e {soma} gols!')