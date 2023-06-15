'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No Final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1OOO.
C) Qual é o nome do produto mais barato.'''

produtos_acima_de_mil = total_gasto = produto_mais_barato = produtos = quantidade_produtos = 0 
nome_produto_mais_barato = ""
print('-'*40)
print('Loja super baratão'.upper().center(30))
print('-'*40)
while True:
    nome_produto = str(input('\nNome do produto: ').capitalize())
    preco = int(input('Preço R$: '))
    quantidade_produtos += 1
    total_gasto += preco

    if quantidade_produtos == 1 or preco < produto_mais_barato:
        nome_produto_mais_barato = nome_produto
        produto_mais_barato = preco

    if preco > 1000:
        produtos_acima_de_mil += 1
    print()

    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Quer continuar ? [S/N] ').upper().strip()[0])
    if continuar[0] == "N":
        print('-'*20,'Fim do programa','-'*20)
        break
    
print(f'''Total da compra foi de R$:{total_gasto:.2f}
temos {produtos_acima_de_mil} produtos custando mais de R$:1000.00 
O produto mais barato foi {nome_produto_mais_barato} custando {produto_mais_barato}''')

# Resolução do curso
print('Resolução do CURSO'.upper().center(40))
total = totmil = menor = cont = 0
barato = " "
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$: '))
    cont += 1
    total += preço

    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ').strip().upper()[0])
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra for R${total:.2f}')
print(f'temos {totmil} produtos custando mais de R$ 1000.00')
