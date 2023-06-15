'''Crie um programa que laia vários números inteiros peloteclado. O programa só vai parar quando o usuário digitar o valor 999, qua é a condiÇáo de parada. 
No Final mostre quantos números Foram digitados e qual Foi a soma entre eles (dasconsidarando o Flag).'''
s = qnt = 0
print()
while True:    
    n = int(input('Insira um número inteiro(999 para parar): '))
    if n == 999:
        break
    qnt += 1
    s += n
print(f'\nforam inseridos {qnt} numeros a soma entre eles é {s}')
