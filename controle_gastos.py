print('\033[33m💰 CONTROLE DE GASTOS 💰\033[m')
print('=' * 20)
alimentacao = 0
transporte = 0
lazer = 0
outros = 0
while True:
    print('[1] Alimentação')
    print('[2] Transporte')
    print('[3] Lazer')
    print('[4] Outros')
    print('[5] Sair')
    opcao = int(input('Escolha: '))
    if opcao == 1:
        valor = float(input('Valor gasto: '))
        alimentacao += valor
    elif opcao == 2:
        valor = float(input('Valor gasto: '))
        transporte += valor
    elif opcao == 3:
        valor = float(input('Valor gasto: '))
        lazer += valor
    elif opcao == 4:
        valor = float(input('Valor gasto: '))
        outros += valor
    elif opcao == 5:
        break
print('\033[36m--- RESUMO ---\033[m')
print(f'Alimentação: R$ {alimentacao:.2f}')
print(f'Transporte: R$ {transporte:.2f}')
print(f'Lazer: R$ {lazer:.2f}')
print(f'Outros: R$ {outros:.2f}')
total = alimentacao + transporte + lazer + outros
print(f'Total gasto: R$ {total:.2f}')