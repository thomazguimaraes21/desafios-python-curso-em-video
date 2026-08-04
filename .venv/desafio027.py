import emoji
nome = str(input('Digite o seu nome: ')).strip().upper()
separa = nome.split()
print('Analisando... Só mais um momento...')
print('===========')
print(emoji.emojize('Analise concluida :check_mark_button:'))
print(f'O seu primeiro nome é: {separa[0]}')
print(f'O seu último nome é: {separa[-1]}')

