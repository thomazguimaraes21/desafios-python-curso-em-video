import random
n1 = random.randint(1, 100) # sorteia os números
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)
n4 = random.randint(1, 100)
n5 = random.randint(1, 100)
t = (n1, n2, n3, n4, n5) # adiciona os números sorteados a tupla
print(f'Os números gerados foram: {t}') # imprime os números sorteados
menor = min(t) # min mostra o menor número
maior = max(t) # max mostra o maior número
print(f'O menor número sorteado foi {menor}')
print(f'O maior número sorteado foi {maior}')