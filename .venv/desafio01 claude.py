# contador de gols
cont = 0
gols = int(input('Digite o número de gols: '))
while gols != -1:
    cont += 1
    gols = int(input('Quantos gols nesse jogo? '))
print(f'O messi fez {cont} gols')


