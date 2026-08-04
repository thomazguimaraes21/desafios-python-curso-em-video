n = int(input('Digite um número: '))
c = n
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else '=', end='')
    c -= 1
print(f'O fatorial de {n} é {c}')