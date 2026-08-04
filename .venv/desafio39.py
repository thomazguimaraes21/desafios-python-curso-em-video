anos = int(input('Digite o seu ano de nascimento: '))
idade = int(input('Digite a sua idade: '))
alistamento = 18
falta = idade - alistamento
if anos == 2008:
    print('Você deve se alistar, está na hora!')
elif anos == 2009:
    print('Está quase na hora de você se alistar! Falta apenas 1 ano!!!!')
elif anos <= 2007:
    print('Já passou da hora de você se alistar!')
    print(f'Fazem {falta} anos que passou para você se alistar!')