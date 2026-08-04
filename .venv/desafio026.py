import emoji
frase = str(input('Digite uma frase: ').upper().strip())
total = frase.count('A')
posição = frase.find('A') + 1
final = frase.rfind('A') + 1
print('Analisando a sua frase....')
print(emoji.emojize('Sucesso na ánalise :check_mark_button:'))
print('===============')
print(f'A letra A aparece {total} vezes na frase.')
print(f'A primeira letra A apareceu na posição {posição}')
print(f'A última letra A apareceu na posição {final}')

