import numpy as np 

print('\n\tMetodo Simpson 3/8 ')

a= 0 #Limite inferior
b= 2 #Limite superior

n=3 #Numero de intervalos , Se tiene que verificar si es valido con el numero de puntos que hay (5)
#puntos = n+1


 # x en funcion de intervalos
x = np.zeros(n+1)
 
 # f(x) en funcion anonima
f = lambda x: x**5

def simpson38 ( a, b, n, x, f):
   h = (b-a) / n
   x[0] = a
   x[n] = b
   
   for k in range( len(x)- 1):
     x[k+1] = x[k] + h
   
   sum1= 0
   sum2= 0
   sum3= 0
   for k in range(1, n-1, 3):
     sum1 += f( x[k])
   for k in range(2, n, 3):
     sum2 += f(x[k])
   for k in range(3, n-2, 3):
     sum3 += f(x[k])
   
   return (3/8) *h *( f(x[0]) + f(x[n]) + 3*sum1 + 3*sum2 + 2*sum3 )

integral  = simpson38(a, b , n, x, f)

print(f'El valor de la integral de x**5, en el intervalo de {a} a {b} es : {integral}')
#10.7037