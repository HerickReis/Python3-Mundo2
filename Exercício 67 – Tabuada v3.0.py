'''Faça um programa que mostre a tabuada de vários números, um de cada vaz. 
para cada valor digitado pelo usuário. 
O programa será intarrompido quando o número solicitado for negativo.'''

# Minha resolução
while True:
    multiplicador = 0
    numero = int(input('Digite um valor: '))
    print('-'*30)
    if numero < 0:
        print('Programa de tabuada encerrado. Volte sempre :)')
        break

    while multiplicador <=10:
        print(f'{numero} X {multiplicador} = {numero * multiplicador}')
        multiplicador += 1
    print('=-' * 20)

# Resoluçao da Aula

while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n} X {c} = {n * c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')