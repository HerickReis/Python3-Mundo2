'''Crie um programa que leia vários números inteiros pelo teclado. 
No Final da execução, mostre a média entre todos os valoras e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuáriob se ele quer ou não continuar a digitar valores.'''

qnt = soma = 0
maior = 0  
menor = 0
r = "S"

while r == "S":
    valores = int(input('Quantos valores quer digitar(Total)? '))

    while qnt != valores :
        n = int(input('Digite um número: '))
        qnt += 1
        soma += n       
        if qnt == 1:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

    r = str(input('Deseja digitar mais valores? [S/N]').upper())

media = soma / qnt
print(f'Foram insiridos {qnt} números, O maior foi {maior} e o menor foi {menor}, a média entre eles foi de {media}')