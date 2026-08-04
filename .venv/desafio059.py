n1 = int(input('Primeiro valor: '))
n2 = int(input(' Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar 
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
       r = n1 + n2
       print(f'A soma dos valores escolhidos é: {r}')

    elif opção == 2:
        r = n1 * n2
        print(f'A multiplicação dos valores escolhidos é: {r}')

    elif opção == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}')
        elif n1 < n2:
            print(f'O número {n1} é menor que o número {n2}')
        else:
            print(f'O número {n1} e o número {n2} são iguais, nenhum é maior!')

    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo o valor: '))

print('Fim do programa! Volte sempre!')