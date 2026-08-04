# cadastro de funcionários sem listas
cont = 0
homens = 0
mulheres = 0
maiores = 0
soma_salarios = 0
maior_salario = 0
menor_salario = 99999999
while True:
    nome = str(input('Digite o seu nome: '))
    idade = int((input('Digite a sua idade: ')))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1
    if idade >= 18:
        maiores += 1
    cargo = str(input('Digite o seu cargo: '))
    salario = float(input('Digite o seu salário: '))
    soma_salarios += salario
    if salario > maior_salario:
        maior_salario = salario
    if salario < menor_salario:
        menor_salario = salario
    cont+= 1
    continuar = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
media_salarial = soma_salarios / cont
print(f'Total cadastrados: {cont}')
print(f'Homens: {homens} | Mulheres: {mulheres}')
print(f'Maiores de 18: {maiores}')
print(f'Média salarial: {media_salarial}')
print(f'Maior salário: {maior_salario}')
print(f'Menor salário: {menor_salario}')