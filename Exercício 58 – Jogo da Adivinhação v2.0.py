'''Malhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar. 
mostrando no Final quantos palpites Foram necessários para vencer.'''
from random import randint
from time import sleep

numeros = randint(0,10)
jogador = tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Pensei em um número entre 0 e 10\nQual número acha que eu pensei? '))
    print()
    tentativas += 1
    if jogador == numeros:
        acertou = True
    else:    
        if jogador < numeros:
            print(f'\n\nHEHE, Não foi {jogador}, Maior\n')

        if jogador > numeros:
            print(f'\nHEHE, Não foi {jogador}, Menor\n')

print(f'Acertou, e foram necessárias {tentativas} tentativas')