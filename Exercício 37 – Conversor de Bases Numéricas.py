'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversÃo:
- 1 para binário
- 2 para octal
- 3 para hexadecimal '''


valor = int(input('Digite um valor inteiro: '))
antes_conversao = valor

# Binario
binario = bin(valor)

# Octal
octal = oct(valor)

# Hexadecimal
hexadecimal = hex(valor)

print('='*20)
print('Escolha para qual base deseja converter')
print('='*20)
print()
print("[1] - Binário")
print("[2] - Octal")
print("[3] - Hexadecimal")

opcao = int(input('digite sua escolha: '))


if opcao == 1 :
    print(f'O valor de {antes_conversao} para binario é: {binario[2:]}')

elif opcao == 2 : 
    print(f'O valor de {antes_conversao} para ocatal é: {octal[2:]} ')

elif opcao == 3  :
    print(f'O valor de {antes_conversao} para Hexadecimal é: {hexadecimal[2:]} ')