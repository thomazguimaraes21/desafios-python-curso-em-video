from datetime import date
atual = date.today().year
anos = int(input('Ano de nascimento: '))
idade = atual - anos
print(f'Quem nasceu em {anos} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos!')