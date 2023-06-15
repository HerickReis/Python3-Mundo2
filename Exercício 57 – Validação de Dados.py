'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valoras 'M' ou 'F' Caso esteja errado, peça a digitação novamenta até ter um
valor correto.'''


sexo = str(input('Digite o sexo [M/F]: ').upper().strip()[0])

while sexo not in 'MmFf':
    print('Valor errado, informe o sexo novamente.')
    sexo = str(input('Digite o sexo: ').upper())

print(f'Sexo {sexo} registrado')