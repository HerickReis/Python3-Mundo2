'''Desenvolva um programa que leia seis números e mostre na tela apenas daquelas que forem pares.
Se o valor digitado for ímpar. Descondidere-o.'''
pares = 0
num = 0
for n in range(1,6):
    numeros = int(input(f'Digite o {n}° número: '))

    if numeros % 2 == 0:
        pares += numeros # Somando os números que estejam dentro de numeros e os passando para variavel pares
        num += 1 # adicionando 1 a cada vez que um numero par for encontrado
print(f'Você forneceu um total de {num} numeros pares e a soma entre eles deu {pares}')