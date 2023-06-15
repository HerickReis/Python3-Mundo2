from time import sleep

n = int(input('Digite um número para verificação: '))
print()
numero = 0

for teste in range(1,n + 1):

    if n % teste == 0:
        #Definindo uma cor para a linha e juntando o proximo print na mesma linha
        #Os valores divisiveis serão exibidos aqui
        print('\033[33m',end=' ')
        numero +=1

    else:
        #Definindo uma cor para a linha e juntando o proximo print na mesma linha
        #Os vaores não divisiveis serão exibidos aqui
        print('\033[31m',end=' ')
    # printando a sequência do loop teste
    print(f'{teste}',end=' ')
sleep(2)


print()
if numero == 2:
    print(f'\n{n} é primo pois é divisivel {numero} vezes')

else:
    print(f'\n{n} não é primo pois foi divisivel {numero} vezes \n')