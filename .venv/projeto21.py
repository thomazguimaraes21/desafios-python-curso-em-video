from random import randint
from time import sleep
import pygame

# ==============================================
# THOMAZ TECHNOLOGIES ©
# Smart Guessing Engine — v1.0.3
# ==============================================

pygame.init()
pygame.mixer.init()

# -------------------------------
# SYSTEM INITIALIZATION
# -------------------------------

print('=' * 60)
print('INITIALIZING SMART GUESSING ENGINE...')
print('=' * 60)

sleep(1)

# -------------------------------
# USER AUTHENTICATION
# -------------------------------

user_name = input('USER IDENTIFICATION: ').strip().title()

print('\nLoading system modules...')
sleep(1)

print('Establishing secure connection...')
sleep(1)

print(f'Welcome, {user_name}.')
print('-' * 60)

# -------------------------------
# RANDOM NUMBER GENERATION
# -------------------------------

system_number = randint(0, 5)

print('The artificial intelligence has generated a number.')
print('Range: 0 to 5')
print('-' * 60)

# -------------------------------
# USER INPUT
# -------------------------------

user_attempt = int(input('ENTER YOUR ATTEMPT: '))

print('\nAnalyzing response...')
sleep(2)

print('-' * 60)

# -------------------------------
# VALIDATION ENGINE
# -------------------------------

if user_attempt == system_number:

    print('STATUS: SUCCESS')
    print(f'Correct answer detected -> [{system_number}]')
    print('User prediction validated successfully.')

    pygame.mixer.music.load('desafio028if.mp3')
    pygame.mixer.music.play()

else:

    print('STATUS: FAILED')
    print(f'Expected value -> [{system_number}]')
    print(f'Received value -> [{user_attempt}]')

    pygame.mixer.music.load('desafio028else.mp3')
    pygame.mixer.music.play()

print('-' * 60)

# -------------------------------
# SESSION FINALIZATION
# -------------------------------

print('Session finalized.')
print('Closing Smart Guessing Engine...')
print('=' * 60)

input('\nPRESS ENTER TO TERMINATE SESSION...')