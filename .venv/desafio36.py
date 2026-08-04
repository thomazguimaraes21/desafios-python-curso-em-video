casa = float(input('Digite o valor da casa desejada: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos deseja pagar a casa: '))
meses = anos * 12
prestação = casa / anos
porcento = salario * 0.30
print(f'A sua parcela será de R${prestação}')
if prestação > porcento:
    print('Desculpe, o seu empréstimo foi negado!')
else:
    print('O seu empréstimo foi aprovado, parabéns!')