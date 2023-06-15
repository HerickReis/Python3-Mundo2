'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
- acima de 40: Obesidade Mórbida'''
import math 
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em cm: '))

if peso <= 0 or altura <=0 :
    print('peso e altura devem ter valores positivos')

altura = altura / 100
imc = peso / (altura ** 2)

if imc <18.5 :
    print(f'Seu imc é de {imc:.2f} você está abaixo do peso.')

elif  18.5<= imc < 25 : 
    print(f'Seu imc é de {imc:.2f} e você está no peso ideal.')

elif 25<= imc <= 30 :
    print(f'Seu imc é de {imc:.2f} e você esta acima do peso.')

elif 30<= imc <=40: 
    print(f'Seu imc é de {imc:.2f} e você está obeso.')

elif imc > 40 :
    print(f'seu imc é de {imc:.2f} e você está com Obesidade Mórbida.')