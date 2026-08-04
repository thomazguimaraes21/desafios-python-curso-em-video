from random import randint
import pygame

pygame.init()
pygame.mixer.init()

computador = randint(0, 5) # Faz o computador ''PENSAR''
print('-==-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar

if jogador == computador:
    print('Parabéns, você acertou!!!')
    pygame.mixer.music.load('desafio028if.mp3.mp3')
    pygame.mixer.music.play()

else:
    print(f'Que pena, você errou, eu pensei em {computador}! Tente novamente')
    pygame.mixer.music.load('desafio028else.mp3.mp3')
    pygame.mixer.music.play()

input('Pressione ENTER para sair...')

