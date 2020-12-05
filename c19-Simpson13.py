import numpy as np

print('\n\tMetodo Simpson 1/3 ')

a= 0 #Limite inferior
b= 2 #Limite superior

n=4 #Numero de intervalos , Se tiene que verificar si es valido con el numero de puntos que hay (5)
 
 
 # x en funcion de intervalos
x = np.zeros(n+1)
 
 # f(x) en funcion anonima
f = lambda x: x**5

def simpson13(a, b, n, x, f): #Simpson 1/3
   h = (b-a) / n
   for k in range( len(x) - 1 ) : 
     x[k+1] = x[k] + h
   
   sum1 = 0
   sum2 = 0
   for k in range(1, int(n/2)+1 ): #Recorriendo todos los elemetos Impares
     sum1 = sum1 + f( x[2*k-1] ) #sumatoria de impares
   for k in range(1, int(n/2  -1) + 1 ):
     sum2 += f( x[2*k] )
   return h* ( f(x[0]) + f(x[n]) + 4*sum1 + 2*sum2  ) /3

integral = simpson13(a, b, n, x, f)

print(f'La integral de x**5 en el intervalo de {a} a {b} es : {integral}')


  