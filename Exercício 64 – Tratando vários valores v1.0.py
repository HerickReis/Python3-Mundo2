'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada.
No Final, mostre quantos números Foram digitados e qual Foi a soma entre eles
(desconsiderando o Flag).'''

qnt = soma = valores = 0
while valores != 999: # Neste programa para desconsiderar o FLAG (ponto de parada (999)) foi feita a adição dos números antes da pergunta
    # Assim garantido que se o valor 999 for inserido ele irá cair na flag e o loop será encerrado sem o adicionar
    qnt += 1
    soma += valores
    valores = int(input('Digite o valor: '))
print(f'Fora digitado {qnt} valores, a soma entre eles é {soma}')