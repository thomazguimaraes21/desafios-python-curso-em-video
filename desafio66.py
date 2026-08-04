n = int(input('Digite um valor (999 para parar): '))
cont = 0
soma = 0
while True:
    soma += n
    cont += 1
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
print(f'A soma dos {cont} valores foi {soma}!')