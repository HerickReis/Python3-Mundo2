'''Faça um programaque leia um número qualquer e mostre o seu Fatorial.
= 5! = 4x3x2x1 = 120'''
n = int(input('Digite um número inteiro para verificação: '))
multiplos = 1
# c recebe o valor de n
c = n
# enquanto multilos for menor que o valor n 
while  multiplos < n:
    # c irá multiplicar e receber o valor de multiplos
    c *= multiplos 
    multiplos += 1

print(f'Resultado de {n}!:',c)