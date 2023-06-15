'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No Final, mostre quantas pessoas ainda não atingiram a maioridade quantas já são
maiores.'''
from datetime import date

atual = date.today().year
menor = 0 
maior = 0

for i in range(1,7+1):
    pessoas = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = atual - pessoas

    if idade >= 21:
        maior += 1

    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade\n e tivemos {menor} menores de idade.')