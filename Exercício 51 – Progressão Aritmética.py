'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,mostre os 10
primeiros termos dessa progressão.'''
from time import sleep
p_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

decimo = p_termo + ( 10-1 ) * razao # Formula matemática para encontrar o termo de um PA
# Para "pa" no intervalo de (inicio) p_termo ,(final) decimo + razao, (ordem) razao
for pa in range(p_termo, decimo + razao, razao):
    print(f'\033[032m{pa}',end='\033[33m -> ')
print('\033[31mACABOU\033[m')