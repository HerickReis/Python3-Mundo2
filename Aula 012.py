nome = str(input('Qual é o seu nome ? '))
if nome == "Herick":
    print('Que nome bonito!'.capitalize())
elif nome == 'Pedro' or nome == 'Joao' or nome == 'Ana' :
    print('Seu nome é bem comum no brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana' :
    print('Belo nome feminino')
print(f'Tenha um bom dia, {nome}')