n = int(input('Digite um valor: '))
while n >= 0:
    for c in range(1, 11):
        tabuada = n * c
        print(f'{c} X {n} = {tabuada}')
    n = int(input('Digite o valor que deseja ver a tabuada: '))
    if n < 0:
        break
print('~' * 10)
print('Fim! Obrigado por participar!!! ☺')

