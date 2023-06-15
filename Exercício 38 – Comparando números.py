'''Escreva um programa que leia dois números inteiros e compare-os,mostrando na tela uma mensagam:
-0 primeiro valor é
maior
-o segundo valor é
maior
-NÃO axista valor
maior. os dois SÃO
iguais'''

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
if valor1 > valor2 :
    print('O primeiro valor é maior')
elif valor2 > valor1 :
    print('O segundo valor é maior')
else:
    print('Nao existe valor maior, os dois são iguais')