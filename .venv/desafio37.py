num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual {hex(num)}')
else:
    print('Opção inválida, tente novamente!')
