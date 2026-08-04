n = int(input('Digite um número: '))
c = 0
s = 0
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número: '))
print(f'Foram mostrados {c} números e a soma deles foi {s}')
print ('FIM')