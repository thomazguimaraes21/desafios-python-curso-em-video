import math
nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota + nota2) / 2
if média <5.0:
    print(f'A sua média foi {média} e você foi REPROVADO!')
elif média > 5 and média <=7:
    print(f'A sua média foi {média} e você está de recuperação!')
elif média >=7.0:
    print(f'Parabéns, a sua média foi {média} e você está APROVADO!Boas férias!')