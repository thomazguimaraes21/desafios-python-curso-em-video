a = int(input('Digite um número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a<=b and a<=c:
    menor = a
if a>=b and a>=c:
    maior = a
if b<=a and b<=c:
    menor = b
if b>=a and b>=c:
    maior = b
if c<=a and c<=b:
    menor = c
if c>=a and c>=b:
    maior = c
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
