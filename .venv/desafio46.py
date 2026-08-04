from time import sleep
import emoji
print('ESTÁ CHEGANDO A HORA')
for c in range(10,-1, -1):
    print(c)
    sleep(0.5)
print(emoji.emojize('\033[1;31mBOOOM\033[m!!FELIZ ANO NOVO :fireworks:'))