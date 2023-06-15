numero_multiplicador = int(input('Digite o numero que deseja realizar a tabuada: '))
for numeros in range (0,10+1):
    resultado = numeros * numero_multiplicador
    print(f'{numero_multiplicador} X {numeros} = {resultado}')
