import numpy as np
import matplotlib.pyplot as plt

n=20
a=0
b=2
h =  (b-a) /n 
x = np.linspace(a, b, n) 
#Funicon f(x) original
f = lambda x: -0.1*x**4 - 0.15*x**3 -0.5*x**2 -0.25*x + 1.2
#Derivada a mano:
fp = lambda x: -0.4*x**3 - 0.45*x**2 - x - 0.25
#Funncion biprima analitica
fpp = -1.2*x**2  -0.9*x - 1

y = f(x)

def derivadaFinita(x, y):
  h= x[1]- x[0]
  n = len(x)
  yp = np.zeros(n) #Segunda tabla
  
  for i in range(n):
    if( i==0 ): #Si estamos en el 1er indice de la tabla ->Progresiva
      yp[i] = (y[i+1] - y[i]) / h
    if( i== n-1 ): #Si estamos en el 1er indice de la tabla -> Regresiva
      yp[i] = (y[i] - y[i-1]) / h
    else:
      yp[i] = (y[i+1] - y[i-1]) / (2*h)
    return yp


yp = derivadaFinita(x, y) #1ramdefivada
ypp = derivadaFinita(x, yp) #Calula recibiendo como parametro la 1ra derivada
plt.plot(x, fp(x), 'r-') #Graficar derivada analitica (a mano)
plt.plot(x, yp, 'bo')
plt.grid(True)
plt.show()
