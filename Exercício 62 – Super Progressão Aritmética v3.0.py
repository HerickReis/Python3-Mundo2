'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos.'''


#Minha resolucao
p_termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razao? '))
termos = int(input('Quantos termos deseja ver? '))
r = 1
print('\033[32m',p_termo,end="\033[31m ->")
while r > 0 :
    termos = termos
    termo = p_termo + (termos-1) * razao
    pa = p_termo
    while pa < termo:
        pa += razao
        print('\033[32m',pa,end=" \033[31m -> ")
    r = int(input('\n\033[34mQuer ver mais quantos termos (Digite 0 para encerrrar o programa) ?\033[m '))
    if r > 0 :
        termos += r
        print(f'\033[32m{p_termo}',end="\033[31m -> ")
        
    else:
        r = 0


#resolução do curso

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->',end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')