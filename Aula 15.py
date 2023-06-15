
# Errado
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print(f'A soma vale {s}')

# Minha resolução
n = s = 0
while n != 999:  
    s += n
    n = int(input('Digite um número: '))
print(f'A soma vale {s}')

# Solução com break
n = s = 0
while True:   
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')