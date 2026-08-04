from random import choice
import emoji

print('=' * 50)
print('      MINI SISTEMA DE COMPRA E SORTEIO')
print('=' * 50)

cliente = input('Digite o nome do cliente: ')
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: R$ '))
desconto = float(input('Digite o desconto (%): '))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print('\n' + '=' * 50)
print('                RESUMO DA COMPRA')
print('=' * 50)
print(f'Cliente: {cliente.upper()}')
print(f'Produto: {produto}')
print(f'Preço original: R$ {preco:.2f}')
print(f'Desconto aplicado: {desconto:.0f}%')
print(f'Valor do desconto: R$ {valor_desconto:.2f}')
print(f'Preço final: R$ {preco_final:.2f}')
print('=' * 50)

nome1 = input('\nDigite o nome do primeiro participante: ')
nome2 = input('Digite o nome do segundo participante: ')
nome3 = input('Digite o nome do terceiro participante: ')
nome4 = input('Digite o nome do quarto participante: ')

ganhador = choice([nome1, nome2, nome3, nome4])

print('\n' + '=' * 50)
print('              SORTEIO PROMOCIONAL')
print('=' * 50)
print(f'O ganhador do brinde foi: {ganhador.upper()}')
print(emoji.emojize('Parabéns ao vencedor! :trophy: :fire:', language='alias'))
print('=' * 50)

metro = float(input('\nDigite uma medida em metros para o frete: '))
cm = metro * 100
mm = metro * 1000

print('\n' + '=' * 50)
print('            CONVERSÃO DE MEDIDAS')
print('=' * 50)
print(f'{metro:.2f} metro(s) equivalem a {cm:.2f} cm')
print(f'{metro:.2f} metro(s) equivalem a {mm:.2f} mm')
print('=' * 50)

print('\nSistema finalizado com sucesso.')
print(emoji.emojize('Projeto concluído :white_check_mark:', language='alias'))