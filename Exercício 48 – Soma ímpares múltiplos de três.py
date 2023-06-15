'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
e que se encontram no intervalo entre 1 e 500'''
quantidade = 0
soma = 0
for numero_impar in range(1,500,2):
        if numero_impar % 3 == 0:
            # Toda vez que um número dentro do intervalo entre 1 e 500 for múltiplo por 3, ele será adicionado a variável soma
            soma += numero_impar
            # Ao ter um número divisível por 3, 1 será adicionado a quantidade
            quantidade += 1
print(f'Com o total de {quantidade} a soma de todos os numeros é {soma}')