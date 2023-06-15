'''Cria um programa que leia a idada e o sexo da várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No Final, mostre:
A) quantas pessoas tam mais da 18 anos.
B) Quantos homens Foram cadastrados.
C) Quantas mulheras tem menos de 20 anos.'''
# Minha resolução
pessoa_cadastrada = homens_cadastrados = mulheres_abaixo_de_20 = pessoa_acima_de_18 = 0
while True:
    print('-'*40)
    print(f'CADASTRE UMA PESSOA'.center(35))
    print('-'*40)

    idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F] ').upper())
    while sexo != "M" and sexo != "F":
        sexo = str(input('Sexo: [M/F] ').upper())
        
    pessoa_cadastrada += 1

    if sexo == "M":
        homens_cadastrados += 1

    if idade >18:
        pessoa_acima_de_18 += 1

    if sexo == "F" and idade < 20:
        mulheres_abaixo_de_20 += 1

    print('-'*40)
    continuar = str(input('\nQuer continuar? [S/N] ').upper().strip())
    while continuar[0] != "S" and continuar[0] != "N":
        continuar = str(input('Quer continuar? [S/N] ').upper().strip())
    print()
    if continuar[0] == "N":
        break

print(f'''\nForam cadastradas {pessoa_cadastrada} pessoas,
Dentre elas são:
{mulheres_abaixo_de_20} mulheres com menos de 20 anos.
{pessoa_acima_de_18} pessoas com mais de 18 anos.
{homens_cadastrados} homens cadstrados''')


# Resolução do curso
print('\nResolução do CURSO')
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ').strip().upper()[0])
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos ? {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')