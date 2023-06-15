'''Faça um programa que mostre na tela uma contagam
ragressiva para o estouro da Fogos de artificio. indo de 10 até
0, com uma pausa de 1 segundos entre eles.'''

import emoji
from time import sleep
import playsound
import pygame

inicio = int(input('Digite o fim da contagem: '))
fim = int(input('Digite o inicio da contagem: '))

pygame.init() # Comando para iniciar o pygame
pygame.mixer.init() # Comando para iniciar o mixer de audio
som = pygame.mixer.Sound("contagem1s.mp3") # Variavel armazenando o mp3 escolhido para reprodução
fogos = pygame.mixer.Sound("fogos_apito.mp3")

for contagem in range(fim, inicio-2, -1): # Para laço contagem no alcance de (fim,inicio-2,-1) print o valor de contagem
    print(emoji.emojize(f'{contagem}'))
    som.play() # Reproduzir som durante contagem.

    for contagem in range(1):
        sleep(1)

print(emoji.emojize('''AEEEE
:fireworks::fireworks::fireworks::fireworks:'''))
playsound.playsound("fogos_apito.mp3")