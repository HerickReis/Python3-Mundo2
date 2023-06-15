'''Faça um programa que leia o peso de cinco pessoas.
No final, mostra qual Foi o maior e o menor peso lidos.'''

menor = 0
maior = 0
for p in range(1,5):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    # Se a primeiro leitura (laço) for igual a 1:
    if p == 1:
        # Tanto menor quanto maior irá receber o valor de peso
        menor = peso
        maior = peso
    # Se a leitura já for maior que 1   
    else:
        # Se o valor armazenado em peso for maior que o armazenado em maior.
        if peso > maior:
            # Maior irá receber o valor de peso (Será atualizado).
            maior = peso
        # Se o valor armazenado em peso for menor que o armazenado em maior.
        if peso < menor:
            # Menor irá receber o valor de peso.
            menor = peso

print(f'O menor peso registrado foi de {menor}kg \nE o maior peso registrado foi de {maior}kg')