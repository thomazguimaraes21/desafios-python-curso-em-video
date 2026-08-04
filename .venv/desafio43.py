peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print(f'O seu IMC atualmente está em {imc:.1f}')
if imc < 18.5:
    print('O seu IMC é: Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('O seu IMC é: Peso ideal. PARABÉNS!')
elif 25 <= imc < 30:
    print('O seu IMC é: Sobrepeso!')
elif 30 <= imc < 40:
    print('O seu IMC é: Obesidade!')
elif imc >= 40:
    print('O seu IMC é OBESIDADE MÓRBIDA! CUIDADO, SE CUIDE!')
