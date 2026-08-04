from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta nascido em {ano} tem {idade} anos')
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')