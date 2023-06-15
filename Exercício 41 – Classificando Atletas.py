'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta a mostre sua categoria. de
acordo com a idade:
Até 9 anos:MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER '''
import datetime

def calcular_idade(data_nascimento) :
    hoje = datetime.date.today()
    idade = hoje.year - data_nascimento.year
    return idade

data_nascimento_str = input('Digite o ano de seu nascimento (DD/MM/AAAA): ')
data_nascimento = datetime.datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
idade = calcular_idade(data_nascimento)
print(idade)

if idade <= 9 :
    print('Olá sua classificação é MIRIM')
elif idade in range(10,14):
    print('Olá sua classificação é JUNIOR')
elif idade in range(15,20):
    print('Olá sua classificação é SÊNIOR')
elif idade >20:
    print('Sua classificação é MASTER')