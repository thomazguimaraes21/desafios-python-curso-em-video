nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é comum no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome feio')
print(f'Tenha um bom dia, {nome}!')