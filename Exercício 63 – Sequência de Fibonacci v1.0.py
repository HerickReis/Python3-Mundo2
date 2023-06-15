'''Escreva um programa qua leia um número n inteiro qualquar e mostre na tela os n primeiros elementos de uma Sequência da Fibonacci.'''

n = int(input('Digite um número para sequência de fibonnaci: '))
s = 3
n2 = n3 = 1
c = n2 + n3
print(f'{n2} -> {n3} -> {c}',end="-> ")
while s < n :
    n2 = n3
    n3 = c
    c = n2 + n3
    s += 1
    print(c,end=" -> ")
print("FIM")