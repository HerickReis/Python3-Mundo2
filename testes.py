'''for repeticao in range(1,3):
    print('Olá',repeticao)
print('Fim')'''

'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for teste in range(i, f+1 , p):
    print(teste)
print('Fim')'''
'''fatorial = int(input('Digite o numero para calcular: '))

for n in range(fatorial , 1 ,- 1):
    c = fatorial * n
    print(c)'''


'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No Final do programa, mostre: A média da idade do grupo, qual é o nome do homem mais velho, Quantas mulheres
tem menos de 20 anos.'''

mulheres_menos_20 = 0
media = 0
for i in range(1,2+1):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ').upper())
    print('~~~~~~~~~~~~~~~~~~~~~')
    print()

    media += idade
    if sexo == "F":
        if idade < 20:
            mulheres_menos_20 += 1

print('Mulheres',mulheres_menos_20, 'media',media)