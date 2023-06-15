'''Escrava um programa para aprovar o empréstimo bancário para a compra de uma casa. 
o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcula o valor da prestação mensal, sabendo que ela não poda exceder 30% do salario ou então o
empréstimo será negado.'''
nome = str(input('Olá qual seu nome? '.capitalize()))
valor_casa = float(input(f'{nome} qual valor da casa? R$: '))
salario = float(input(f'{nome} qual seu salário atual ? R$:'))
quantos_anos = int(input(f'{nome} em quantos anos pretende quitar a casa ?: '))
anos = quantos_anos * 12

taxa_juros_anual = 0.085
taxa_juros_mensal = taxa_juros_anual / 12
valor_prestacao = (valor_casa * taxa_juros_mensal) / (1-(1+taxa_juros_mensal) ** - anos)
total = salario + (quantos_anos * valor_casa/100)

if valor_prestacao > salario * 0.3:
   print(f"Infrelizmente o empréstimo não pode ser liberado\n Pois o valor de {valor_prestacao:.3f} corresponde a mais de 30% de seu salário")

else:
   print(f"O empréstimo foi liberado no valor de \nPrestação mensal {valor_prestacao:.3f}")