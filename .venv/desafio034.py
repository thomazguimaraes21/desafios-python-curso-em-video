salário = float(input('Digite o seu salário atual: '))
if salário >= 1250:
    aumento = salário * 0.15
    novo = salário + aumento
    print(f'O seu salário ganhou um aumento de 15%, deixou de ser {salário} e passou a ser: R${novo:.2f}')
else:
    salário <= 1250
    aumento = salário * 0.10
    novo = salário + aumento
    print(f'O seu salário ganhou um aumento de 10%, deixou de ser {salário} e passou a ser: RS{novo:.2f}')
