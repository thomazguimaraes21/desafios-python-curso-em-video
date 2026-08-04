Km = float(input('Digite a distância da sua viagem em Km: '))
preço = Km
if Km < 200:
    preço = Km * 0.50
    print(f'A sua viagem foi de {Km}Km e custou R${preço:.2f}')
else:
    preço = Km * 0.45
    print(f'A sua viagem foi de {Km}Km e custou R${preço:.2f}')
