'''Faça um programa que leia o ano de nascimento de um jovem e informa. de acordo com sua idade:
-Se ele ainda vai se
alistar ao serviço
militar.
-Se é a hora da sa
alistar.
-Se já passou do
tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from time import sleep
from datetime import date as dt

nome = str(input('Digite seu nome: ').capitalize())
print()
print('Espere um momento')
sleep (1)
print()

cores = {"Limpa" : '\033[m',    # Biblioteca de cores
         "Azul" : '\033[1;34m',
         "Verde" : '\033[1;32m',
         "Vermelho" : '\033[1;31m'
}

atual = dt.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

tempo_que_passou = idade - 18 # subtração da idade digitada por 18 caso a pessoa tenha mais de 18 anos.
tempo_que_falta = 17 - idade # Subtração de idade para verificar quantos anos faltam para o alistamento.

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
sleep(1)

 # Se a idade for menor que 17 anos irá executar o camando print
if idade <17 :
    print(f'''{cores["Azul"]}Olá voce ainda nao pode se alistar, para se alistar você precisa ter pelo menos 17 anos e ainda faltam {tempo_que_falta} anos 
Então seu alistamento será em {nasc + 18}.{cores["Limpa"]}''')

    exit() # comando para encerrar o programa caso o usuario tenha menos de 17 anos

print()
print('='*20)
print('Escolha seu sexo')
print()
print('[1] Masculino')
print('[2] Feminino')
print('='*20)
print()
sexo = str(input('Escolha seu sexo de acordo com as opções acima: '))

if sexo == '1' :
    print()
    print('Você é homem e deve se alistar.')
else :
    print()
    print('Você é mulher e não precisa se alistar.')
  
print()
print('='*20)
print()
print('Deseja Continuar ?')
print('[1] Sim')
print('[2] Não')
print('='*20)
print()

opcoes = str(input('Escolha se deseja continuar? (escolha de acordo com as opções acima): '))

if opcoes == '1' :
    print('Ok! vamos continuar ')

else :
    print('Você escolheu sair ')
    exit()

#Menu de interação do usuário
print()
print('_'*20)
print()
print('Voce já se alistou? ')
print('[1] - Sim')
print('[2] - Nao')
print('_'*20)
print()

# Irá receber a resposta do usuário para a questão do menu acima.
opcao =str(input(f'{nome} escolha entre  sendo [1] para Sim e [2] para Nao: ')) 

# Caso o usuario digite um valor inválido o While entrará em ação fazendo novamente a pergunta ao usuário

while  opcao != '1' and opcao != '2' :  # Se o valor de opcao for diferente "!=" de 1 ou 2 a pergunta será refeita
    opcao =str(input(f'{nome} escolha entre sim ou nao, sendo [1] para Sim e [2] para Nao: '))
    break # quebrar o loop da escolha, gerando assim atualização na resposta


print('Analisando...')
sleep(1.2) # Uma pequena pausa antes de exibir o resultado


'''if opcao != '1' and opcao != '2' : # se o valor da variavel opcao for diferente "!=" de 1 ou 2 o programa irá refazer a pergunta (Inútil por conta do while)
    print(f'{cores["Vermelho"]}Por favor escolha entre [1] e [2].{cores["Limpa"]}')'''

# Se a pessoa tiver 17 anos e Não tiver se alistado irá exibir a mensagem dizendo que já está na hora
if idade == 17 and opcao == '2':
    print(f'{cores["Azul"]}{nome} Já está na hora de se alistar.{cores["Limpa"]}')

# Se a pessoa tiver 17 anos e se alistou irá exibir a mensagem o parabenizando
elif idade == 17 and opcao == '1' :
    print(f'{cores["Verde"]}Muito bem {nome} então você já se alistou !.{cores["Limpa"]}')

# Se for maior de 18 anos e nao se alistou irá exibir a mensagem dizendo quanto tempo se passou do alistamento
elif idade > 18 and opcao == '2' : 
    print(f'''{cores["Vermelho"]}{nome} Você ultrapassou {tempo_que_passou} ano/s da idade de alistamento
Seu alistamento foi em {nasc + 18 }.{cores["Limpa"]}''')

# Se a pessoa for maior de 18 anos de se Alistou irá exibir a mensagem o parabenizando
elif idade > 18 and opcao == '1' :
    print(f'{cores["Verde"]} que bom que voce ja alistou {nome}{cores["Limpa"]}')

# Se a pessoa tiver 18 anos e se alistou irá exibir a mensagem o parabenizando.
elif idade == 18 and opcao == '1' :
    print(f'{cores["Verde"]}Ótimo {nome} você ja alistou. {cores["Limpa"]}')
    
# Se a pessoa tiver 18 anos e nao se alistou irá exibir dizendo que ele ainda não se alistou
elif idade == 18 and opcao =='2' :
    print(f'''{cores["Vermelho"]}{nome} voce já deveria ter se alistado. 
Pois seu alistamento foi em {nasc + 18}{cores["Limpa"]}''')

print('='*20)
print('Obrigado por utilizar o programa. \n Até mais.')