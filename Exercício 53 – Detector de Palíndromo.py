'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
deconsiderando os espaços'''
from time import sleep

cores = {
    "entrada" : '\033[33m',
    "analise" : '\033[1;34m',   # Definindo biblioteca de cores
    "positivo":'\033[32m',
    "negativo" : '\033[31m',
    "fim" : '\033[m'
        }

frase = str(input(f'{cores["entrada"]}Digite uma frase ou palavra para verificação: {cores["fim"]}').replace(" ","").strip().upper())

for f in range(10):
    palindromo = frase[::-1] # Invertendo a ordem da escrita.

    print(f'{cores["analise"]}Verificando...{cores["fim"]}\n') 
    sleep(2)

    # Se frase for igual a frase invertida é um palíndromo
    if frase == palindromo :
        print(f'{cores["positivo"]}"{frase}" ao contrário fica:\n\n{frase.replace(" ","")}\n\nÉ um palíndromo!! {cores["fim"]}') 

    # Caso contrário não é um palíndromo
    else:
        print(f'{cores["negativo"]}"{frase}" ao contrário fica {frase.replace(" ","")} ao contrário fica \n{palindromo} \nentão não é um palíndromo !{cores["fim"]}')

    analise = print(f'\nAnalise {f+1}/10\n')
    frase = str(input(f'{cores["entrada"]}Digite outra frase ou palavra para verificação: {cores["fim"]}').replace(" ",""))
    
    print()
    palindromo = frase [::-1]