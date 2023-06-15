'''Crie um programa que simule o Funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual sará o valor a ser sacado (número inteiro) e o programa vai inFormar quantas cédulas de cada valor serão entregues.
OBS: 
considere que o caixa possui cédulas de
R$50, R$20, R$10 e R$ 1.'''
print('=-'*40)
print('seja bem-vindo ao banco quase quebrado'.upper().center(35))
print('=-'*40)

valor_cedulas = (50, 20, 10 , 1)
while True:
    quantia_sacada = int(input('Valor do saque: '))
    print()
    print('='*80)
    quantia_restante = quantia_sacada

    cedulas_50 = int(quantia_restante / valor_cedulas[0])
    quantia_restante -= cedulas_50 * valor_cedulas[0]  

    cedulas_20 = int(quantia_restante / valor_cedulas[1])
    quantia_restante -= cedulas_20 * valor_cedulas[1]

    cedulas_10 = int(quantia_restante / valor_cedulas[2])
    quantia_restante -= cedulas_10 * valor_cedulas[2]

    cedulas_1 = int(quantia_restante / valor_cedulas[3])
    quantia_restante -= cedulas_1 * valor_cedulas[3]

    if cedulas_50 > 0:
        print(f'Total de {cedulas_50} cédulas de R$ 50 ')
    
    if cedulas_20 > 0:
        print(f'Total de {cedulas_20} cédulas de R$ 20')
    
    if cedulas_10 > 0:
        print(f'Total de {cedulas_10} cédulas de R$ 10')
    
    if cedulas_1 > 0:
        print(f'Total de {cedulas_1} cédulas de R$ 1')
    print('='*80)
    print('Volte sempre ao Banco QUASE quebrado\nObrigado pela preferência e Tenha um Bom dia!\n:D')
    break

# Resolução do curso
print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
valor = int(input('Que valor você vai sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        if céd == 20:
            céd = 10
        if céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! tenha um bom dia!')