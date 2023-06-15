'''Rafaça o DESAFIO 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

#Minha resolução
'''p_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimo = p_termo + (10-1) * razao
pa = p_termo
while pa < decimo:
    pa += razao
    print('\033[32m',pa,end='\033[31m -> ')
print('\033[32mFIM\033[m')'''



#resolução do curso
print('Gereador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->',end='')
    termo += razao
    cont += 1
print('FIM')