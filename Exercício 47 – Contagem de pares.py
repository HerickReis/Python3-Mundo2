'''Crie um programa que moestre na tela todos os números pares que estão no intervalor entre
1 e 50.'''
from time import sleep
def linha():
    print("-_-"*20)

print()
linha()
print('Números Pares')
linha()
print()
for numeros_pares in range(0,50+1,2):
    print('.',end='')
    if numeros_pares % 2 == 0 :
        print(numeros_pares,end=" -> ")
sleep(2)

print()
linha()
print('Números Ímpares')
linha()
print()

for numeros_impares in range(0,51): 
    if numeros_impares % 2 == 1 :
        print(numeros_impares,end=" -> ")