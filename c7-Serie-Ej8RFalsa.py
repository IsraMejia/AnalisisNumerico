
import numpy as np

print('\n\tInterpolacion de valores o regla falsa \n')

def rf(a,b): #Regla falsa
    return  b-f(b)*(a-b) / ( f(a) - f(b))

def f(x): #Funcion del ejercicio
    return np.power(x, 4) + 9*np.power(x,3) + 9*np.power(x,2) - 8*x -12


a = 1  #Limite inferior intervalo
b= 2    #Limite superior intervalo
tolerancia = 0.01

cabecera = "{:<8}   {:<10}  {:<10}  {:<10}  {:<10}  {:<10}  {:<10}".format( 'It' , 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'  )
# {:<8} =>8 Espacios en blanco, 1 celda de la tabla     Se les asigna el nombre a la celda
print(cabecera)

it=1

while True:
    c = rf(a, b)
    fa = f(a)
    fb = f(b)
    fc = f(c)

    fila = "{:<8} {:<8.4g} {:<8.4g} {:<8.4g}   {:<8.4g}   {:<8.4g}   {:<8.4g}".format( it, a, b, c, fa, fb, fc)
    print(fila)
    
    if( abs(f(c)) < tolerancia ):
        print('\n\tRaiz encontrada')
        print("\t\t\t{:0.4g}".format(c) )
        break
    
    elif(fa*fc) < 0 : #Si cambio el signo
        b=c #Nuevo limite superior
    elif(fb*fc) <0:
        a = c #Nuevo limite inferior
    else:
        print("No hubo cambio de signo, elige un nuevo intervalo")
        a = float(input("Introduce limite inferior :"))
        b = float(input("Introduce limite superior :"))
    
    it +=1
    



