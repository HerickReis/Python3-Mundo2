'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 a 6.9:
RECUPERAÇÃO
-Média 7.0 ou superior:
APROVADO'''
nome_do_professor = str(input('Professor informe seu nome: ')).title().strip()
nome_do_aluno = str(input('Digite o nome do aluno: ')).title().strip()

cores = { "Limpa" : '\033[m',
         "Aprovado" : '\033[1;32m',
         "Reprovado" : '\033[1;31m',
         "Recuperacao" : '\033[33m'
}

print('='*20)
print('[1] - Matemática')
print('[2] - História')
print('[3] - Geografia')
print('[4] - Ciências')
print('[5] - Português')
print('[6] - Inglês')
print('[7] - Artes')
print()
print('='*20)

opcoes = int(input('Professor digite a opção de acordo com sua matéria: '))
materia = opcoes

if opcoes == 1:
    materia = 'Matemática'
elif opcoes == 2:
    materia = 'História'
elif opcoes == 3:
    materia = 'Geografia'
elif opcoes == 4:
    materia = 'Ciências'
elif opcoes == 5:
    materia = 'Português'
elif opcoes == 6:
    materia = 'Inglês'
elif opcoes == 7:
    materia = 'Artes'
else:
    materia = 'Opção inválida'

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2

if media < 5.0 :
    print(f'{cores["Reprovado"]}Prof {nome_do_professor} o aluno {nome_do_aluno} foi reprovado em {materia} com média {media}{cores["Limpa"]}')

elif media == 5.0 or media == 6.9 : 
    print(f'{cores["Recuperacao"]}Prof {nome_do_professor} o aluno {nome_do_aluno} ficou de recuperação em {materia} com média {media}{cores["Limpa"]}')

elif media >= 7.0:
    print(f'{cores["Aprovado"]}Prof {nome_do_professor} o aluno {nome_do_aluno} foi aprovado em {materia} com média {media}{cores["Limpa"]}')