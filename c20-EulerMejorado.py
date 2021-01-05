print('Método Euler')

import numpy as np
import matplotlib.pyplot as plt

#Condicionales Iniciales  y datos
x0=0
y0=1
xf=5
h=0.01 #Entre menor la h es mejor la aproximacion :)
#Ecuación diferencial
f= lambda x,y: 2*y+4*x+2

#Aplicando el método de Euler
def Euler(x0, y0, xf, h, f):
  a= x0
  b= xf
  n =(b-a) / h
  x = np.zeros(int(n+1))
  y = np.zeros(int(n+1))
  x[0] = x0
  y[0] = y0 
  for i in range(int(n)):
    x[i+1] = x[i]+ h
  for i in range(int(n)):
    m1 = f(x[i], y[i])
    u = y[i] + (h* m1)
    m2 = f( x[i], u)
    y[i+1] = y[i] + (0.5* h * ( m1+ m2))
  return x,y 

xs , ys = Euler(x0, y0, xf, h, f)  #variables de solucion

ya = lambda x: -(2*x) -2 + 3*(np.exp(2*x))  #Solucion Analitica
#ya = lambda x: -2*x -2 + 3*(2.718)**(2*x) 
xd = 'Solucion Numerica h='+ str(h)
plt.plot(xs, ys, label= xd )
plt.plot( xs, ya(xs), label= 'Solucion Analitica' )
plt.legend()
plt.grid()
plt.show() 