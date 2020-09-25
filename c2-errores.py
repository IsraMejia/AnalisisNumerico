from math import factorial 
print("\n\n\t Calculando tipos de Errores para el numero de Euler\n")

#valorReal = 2.71828 #Cuando sabemos el valor real lo podemos definir asi
#eAprox = 1 # El primer termino de la sumatoria de Euler
#eAprox = 1 + 1/1 # El Segundo termino de la sumatoria de Euler
#eAprox = 1 + 1 + 0.5 # El Tercer termino de la sumatoria de Euler
#eAprox = 1 + 1 + 0.5 + (1/6) # El Cuarto termino de la sumatoria de Euler
#eAprox = 1 + 1 + 0.5 + (1/6) + (1/24) # El Quinto termino de la sumatoria de Euler

"""En la vida real no conocemos el valor real, entonces tenemos que hacer
definir un termino y tomarlo como el valor real temporal """
valorReal = 1/factorial(0)
print(f'El valor real inicial es {valorReal}  = 1/0!')
eAprox = 0 


"""Para no estar calculando cada valor aproximado se usara un ciclo """

for n in range (1,5): #de 1 a 5, 4 pasos en total
    eAprox =valorReal + 1/factorial(n)
    print(f'\nEstamos en el termino {n+1} del calculo')
    print(f'\tEl valor de   eAproximado: {eAprox}')

    errorAbsoluto = abs(valorReal - eAprox)
    print(f'El error Absoluto es: {errorAbsoluto}')

    errorRelativo = errorAbsoluto/abs(valorReal)
    print(f'El error Relativo es: {errorRelativo}')

    errorRPorcentual = errorRelativo * 100
    print(f'El error Relativo Porcentual es: {errorRPorcentual} \n')

    valorReal = eAprox #Actualizamos el Valor relativo y reducir deltas