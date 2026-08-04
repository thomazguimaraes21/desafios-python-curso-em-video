valor = input('Digite o valor: ').replace('.', '').replace(',', '.')
valor = float(valor)
print('[1] Dinheiro')
print('[2] Cartão à vista')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
forma = int(input('Digite a forma de pagamento: '))
desc1 = valor * 0.10
desc2 = valor * 0.05
juros = valor * 0.20
final = valor - desc1
final2 = valor - desc2
final3 = valor + juros
if forma == 1:
    print(f'Você pagou R${valor} em dinheiro, o seu desconto é de 10% e ficou: R${final:.2f}')
elif forma == 2:
    print(f'Você pagou R${valor} no cartão à vista, o seu desconto é de 5% e ficou: R${final2:.2f}')
elif forma == 3:
    print(f'Você pagou R${valor} em 2x no cartão!')
elif forma == 4:
    print(f'Você pagou R${valor} em 3x ou mais no cartão e o juros é de 20%, o valor final ficou: R${final3:.2f}')