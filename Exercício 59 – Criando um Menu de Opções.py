'''Crie um programa
que leia dois valoras e mostre um manu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
operacao = 1
numero_1 = 0
numero_2 = 0

for num in range(2):
    n = float(input('Insira os números para calcular: '))
    if num == 0:
        numero_1 = n
    else:
        numero_2 = n

# Loop verificando condições
while operacao > 0:
    resultado = 0
    maior = menor = 0

    print()
    print("-"*20)
    print()
    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa''')
    print()
    print("-"*20)
    print()
    operacao = int(input('Escolha a operação a ser executada: '))
    sleep(1)

            # Operações matemáticas
    if operacao == 1:
            print('\nVocê escolheu somar\n')
            print()
            resultado  = numero_1 + numero_2
            print(f'{numero_1} + {numero_2} é: {resultado}')
            sleep(1)
        
    elif operacao == 2:
            print('\nVocê escolheu multiplicar\n')
            print()
            resultado = numero_1 * numero_2
            print(f'O resultado para {numero_1} X {numero_2} é : {resultado}')
            sleep(1)

    elif operacao == 3:
            print('\nVocê escolheu verificar o maior valor\n')
            print()
            if numero_1 > numero_2:
                maior = numero_1
            else:
                maior = numero_2
            
            if numero_2 < numero_1:
                menor = numero_2

            else:
                menor = numero_1

            print(f'\nO maior número é {maior} e o menor é {menor}\n')
            sleep(1)

    elif operacao == 4:
        print('\nVocê quer ecolher novos números\n')
        for num in range(2):
            numeros = float(input('Insira os novos números: '))
            if num == 0:
                numero_1 = numeros
            else:
                numero_2 = numeros

    elif operacao == 5:
        print('\nVocê decidiu encerrar o programa\n')
        operacao = 0
        sleep(1)
    
    else:
        print('\nOperação inválida tente novamente.\n')
        sleep(1)
print('FIM')
