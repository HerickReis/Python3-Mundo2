'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No Final do programa, mostre: A média da idade do grupo, qual é o nome do homem mais velho, Quantas mulheres
tem menos de 20 anos.'''

femininos_menor_20 = 0
maior = 0
menor = 0
media = 0
nome_maior = ""
menor_nome = ""
media = 0

for i in range(1,4+1): 
    print(f'~~~~~~~{i}° Pessoa~~~~~~~')
    nome = str(input(f'Nome: ').capitalize().strip())
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M] -Masculino [F] -Feminino: ').upper())
    print('~'*70)
    print()

    media += idade
    if sexo == "F" or sexo == "M":
        if idade < 20:
            femininos_menor_20 += 1

    elif sexo == "M" or sexo == "H":
        media += idade
        # Se a primeira leitura(laço) for igual a 1:
        if i == 1:
            # Ambas terão o mesmo valor tanto menor quanto maior
            maior = idade
            menor = idade         
        # Se já houver mais de uma leitura
        else:
            # Se o valor atual de idade for maior que o valor armazenado em maior 
            if idade > maior:
                # Maior irá receber o valor de idade
                maior = idade
                nome_maior = nome
            # Se o valor atual de idade for menor que o valor armazenado em menor
            if idade < menor:
                #Menor irá receber o valor de idade
                menor = idade
                menor_nome = nome
    else :
        print('\n\033[31mOPÇÂO INVÀLIDA. INSIRA OS DADOS NOVAMENTE:\033[m\n')
        print(f'~~~~~~~{i}° Pessoa~~~~~~~')
        nome = str(input(f'Nome: ').capitalize().strip())
        idade = int(input(f'Idade: '))
        sexo = str(input(f'Sexo [M] -Masculino [F] -Feminino: ').upper())
        print('~'*70)
        print()

print(f'A média de idade do grupo é {media/4}.\nO homem mais velho é {nome_maior} com {maior} anos, o mais novo {menor_nome} com {menor} anos.\nO grupo tem {femininos_menor_20} Mulheres com menos de 20 anos')