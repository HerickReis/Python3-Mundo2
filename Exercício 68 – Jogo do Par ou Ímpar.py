'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no Final do jogo.'''
# Minha resolução
from random import randint
cores = {
'Aguarda' : "\033[33m",
'Perdeu' : "\033[31m",
'Venceu' : "\033[32m",
'Fim' : "\033[m"
}
vitoria = 0
while True:
    pc = randint(0,10)  

    jogador = int(input('Diga um número: ').strip())
    par_impar = str(input('Par ou ímpar [P/I]: ').upper().strip())
    total = jogador + pc
    resultado = total % 2
    while par_impar not in 'PI':
        par_impar = str(input('Par ou ímpar [P/I]: ').strip().upper()[0])
    print('-='*30)

    if resultado == 0:
        venceu_perdeu = "PAR"

    else:
        venceu_perdeu = "IMPAR"

    print(f'\n{cores["Aguarda"]} Você jogou {jogador} e o computador jogou {pc}. Total de {total} DEU {venceu_perdeu} {cores["Fim"]}\n')
    print('=-'*30)

    if par_impar[0] == "I":
        if venceu_perdeu == "PAR":
            print(f'{cores["Perdeu"]} Você perdeu {cores["Fim"]}')
            print('-'*40)
            print(f'GAME OVER! voce venceu {vitoria}')
            break
        else:
            print(f'{cores["Venceu"]} Você ganhou {cores["Fim"]}')
            vitoria += 1

    elif par_impar[0] == "P":
        if venceu_perdeu == "IMPAR":
            print(f'{cores["Perdeu"]} Você perdeu {cores["Fim"]}')
            print('-'*40)
            print(f'GAME OVER! voce venceu {vitoria} vezes')
            break
        else:
            print(f'{cores["Venceu"]} Você ganhou {cores["Fim"]}')
            vitoria += 1
    print('-='*30)


# Resolução do curso

from random import randint
v = 0
while True:
    jogador = int(input('Diga um Valor: '))
    computador = randint(0,10)
    total = jogador +  computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input('Par ou Ímpar? ').strip().upper()[0])
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}',end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente...')
print(f'GAME OVER! Você perdeu\nhouve {v} vitórias :()')