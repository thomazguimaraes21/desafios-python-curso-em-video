gols_pro = int(input('Digite o número de gols do seu time: '))
gols_contra = int(input('Digite o número de gols do adversário: '))
total = gols_pro + gols_contra
if total % 2 == 0:
    print(f'O seu time marcou {gols_pro} gols e o adversário {gols_contra}, dando um total de {total} gols na partida e os gols foram PAR')
else:
    print(f'O seu time marcou {gols_pro} gols e o adversário {gols_contra}, dando um total de {total} gols na partida e os gols foram ÍMPAR')