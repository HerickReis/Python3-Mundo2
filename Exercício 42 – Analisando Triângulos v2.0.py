'''Rafaça o DESAFIO 035 dos triângulos.
acrescentando o recurso de mostrar que tipo de triângulo será formado:

-Equilátero: todos os
lados iguais
-Isóscelas: dois lados
iguais
-Escalano: todos os lados diferentas'''

lado_A = float(input('Informe o cumprimento A do triângulo: '))
lado_b = float(input('Informe o cumprimento B do triângulo: '))
lado_c = float(input('Informe o cumprimento C do triângulo: '))

if (lado_A + lado_b < lado_c) or (lado_b + lado_c < lado_A) or (lado_c + lado_A < lado_b) :
    print('Não é um triângulo. ')

# Se os lados A, B e C forem iguais o triângulo é Equilátero
    if lado_A == lado_b and lado_b == lado_c and lado_A == lado_c:
        print('O triângulo é Equilátero pois todos os lados são iguais.')

# Caso dois lados possuirém dois valores igauis o triângulo será isóceles
    elif lado_A == lado_b or lado_b == lado_c or lado_c == lado_A :
        print('O triângulo é isóceles pois possui dois lados iguais.') 

# Caso os lados A, B e C forem todos diferentes o triângulo será escaleno
    elif lado_A != lado_b and lado_c != lado_b :
        print('O triângulo é escaleno pois todos lados são diferentes.')
# Neste caso encontrei duas possibilidades para resolver o triângulo escaleno, a primeira, seria utilizando a variável else, que exibiria o valor se nenhuma das condições acima fossem válidas.
'''else :
    print('O triângulo é escaleno pois todos lados são diferentes.')'''


# A segunda seria a variável elif acima, que compara os valores utilizando o valor diferente de "!=".
'''elif lado_A != lado_b and lado_c != lado_b :
    print('O triângulo é escaleno pois todos lados são diferentes.')'''
