from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Deu empate!')

    elif jogador == 1:
        print('Parabéns, você ganhou!')

    elif jogador == 2:
        print('Você perdeu!')

    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou papel
    if jogador == 1:
        print('Deu empate! Ambos jogaram PAPEL!')

    elif jogador == 0:
        print('Você perdeu!')

    elif jogador == 2:
        print('Parabéns, você ganhou!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # computador jogo tesoura
    if jogador == 2:
        print('Deu empate! Ambos jogaram TESOURA.')

    elif jogador == 1:
        print('Você perdeu!')

    elif jogador == 0:
        print('Parabéns, você ganhou!')

    else:
        print('JOGADA INVÁLIDA!')

