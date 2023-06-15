import random
from time import sleep
opcoes = ["Pedra","Papel","Tesoura"]

computador = random.choice(opcoes)
usuario = str(input('Escolha entre Pedra, Papel e Tesoura: ').capitalize())
escolha = print(f'Sua escolha foi {usuario}\nE o computador escolheu {computador} Então\n')

sleep(1)
while True :
    if computador == "Pedra" and usuario == "Papel" :
        print('Parabéns você ganhou :D')
        break

    elif computador == "Papel" and usuario == "Tesoura" :
        print('Parabéns voce ganhou :D')
        break

    elif computador == "Tesoura" and usuario == "Pedra" : 
        print('parabéns você ganhou :D')
        break

    elif computador == usuario :
        print('Deu empate HEHE')
        break

    else :
        print('Você Perdeu D: ')
    
