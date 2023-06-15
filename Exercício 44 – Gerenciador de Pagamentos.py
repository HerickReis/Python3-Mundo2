'''Elabore um programa qua calcula o valor a ser pago por um produto, considerando o seu
praço normal a condição de pagamento:
— à vista dinheiro/
cheque: 10% de
desconto
— à vista no cartão: 5%
de desconto
— em até 2x no cartão:
preço normal
— 3x ou mais no cartão:
20% de juros'''

from time import sleep

print(f'\n\033[1;31m{" Lojas Kikinho ":=^40}\n\033[m')
valor_produto = float(input('Digite o valor do produto: '))

print('='*20)
print()
print('Opções de pagamento')
print('[1] Á vista (10% de desconto)')
print('[2] Á vista no cartão (5% de desconto)')
print('[3] 2x no cartão (sem desconto)')
print('[4] 3x ou mais (20% de juros)')
print()
opcoes = int(input('Escolha a opção de pagamento de acordo com a opção desejada: '))

print()
print('Ok! opção de pagamento escolhida, vamos realizar o cálculo do valor de seu produto.\nPor favor aguarde um instante...')
sleep(1.5)
print()
if opcoes == 1 :

    desconto_10 = valor_produto - (valor_produto * 10 / 100) # Desconto de 10% no valor total do produto.
    print(f'O pagamento do produto será a vista no dinheiro/cheque então o valor com 10% de desconto será de {desconto_10}\n')

elif opcoes == 2 : 

    desconto_5 = valor_produto - (valor_produto * 5 / 100) # Desconto de 5% no valor total do produto.
    print(f'O pagamento será a vista no cartão então o valor com 5% de desconto será de {desconto_5}\n')
    
    
elif opcoes == 3: 

    valor_prestação_2x = valor_produto / 2 # Neste caso o valor das prestações em 2x nao há desconto nem juros, entao o valor total será dividido em duas parcelas.
    print(f'O pagamento do produto será em 2x no cartão então o valor das prestações será de {valor_prestação_2x}\n')

elif opcoes == 4:

    print(f'O pagamento será parcelado em 3 vezes ou mais\n')

    sleep(1)
    parcelas = int(input('Digite a quantidade de vezes que deseja parcelar: '))
    print()
    valor_com_juros = valor_produto * 120 # Aqui o calculo esta sendo 20% por cento acima de 100% do valor total do produto 
    valor_prestacao = (valor_com_juros /100) / parcelas # divisao do valor com juros nas parcelas necessarias

    print(f'O valor do produto mensal com 20% de juros será de R$: {valor_prestacao}\nO valor total de sua compra parcelada em {parcelas}vezes será de R$: {valor_prestacao * parcelas}')
    
else :

    print('\033[1;31m Opção inválida!\033[m')

print()
print('Obrigado Por utilizar o progarama. Até mais :D')
print()
print()