#Método del trapecio
import numpy as np

#Límite Inferior
a=0
#Límite Superior
b=2
#Intervalos
n=10
#Obteniendo h
h=(b-a)/n
#Obteniendo x
x=np.zeros(n+1)
print(h)
for k in range(n+1):
  x[k]=a+k*h
print(x)

f= lambda x: x**5 

def trapecio(a,b,n,x,f):
  h=(b-a)/n
  sum=0
  #Suma los puntos intermedios
  for k in range(1,n):
    sum=sum+f(x[k])
  return h*( (f(x[0])+f(x[n]))/2+sum )

integral = trapecio(a,b,n,x,f)
print("La integral de x**5 entre 0 y 2 es: ", integral )

Ea = abs(10.66 - integral)
Erp = (Ea / abs(10.667) ) * 100
print(f'Ea = {Ea}')
print(f'Erp = {Erp}')