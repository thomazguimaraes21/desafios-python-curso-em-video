from random import randint
vitorias = 0
while True:
    computador = randint(0, 10)
    usuario = int(input('Escolha um número: '))
    palpite = input('Você acha que a soma vai ser par ou ímpar? ')
    soma = computador + usuario
    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    if palpite == resultado:
        vitorias += 1
    else:
        print(f'Você perdeu! Total de vitórias: {vitorias}')
        break
