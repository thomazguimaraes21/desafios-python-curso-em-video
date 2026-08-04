p = int(input('Digite quantas pessoas entraram no bar: '))
cont = 0
soma = 0
while p != -1:
    soma += p
    cont += 1
    p = int(input('Digite quantas pessoas entraram no bar: '))
print(f'{soma} pessoas entraram no bar!')
print('Fim')