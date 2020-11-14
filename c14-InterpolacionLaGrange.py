import numpy as np
import sympy as sym #Para matematica simbolica, como matlab, pero cool en python xd
import matplotlib.pyplot as plt

print('Interpolacion de valores por el Polinomio')
print('\t\t LaGrange')

#Datos de la tabla 
xi = np.array([-1, 0, 1])
yi = np.array([2, 1, 3])

def IntLagrange(xi , yi):
  n = len(xi)
  x = sym.Symbol('x') #Le indicas que lo identifique como algebraico simbolica
  polinomio = 0 #El valor inicial 100pre es 0

  #Sumatoria
  for i in range(0, n):
    numerador = 1 #Identico multiplicacion
    denominador = 1 #Identico multiplicacion

    #Productorio
    for j in range(0, n):
      if (i != j): #Para que no se indetermine
        numerador = numerador * (x - xi[j])
        denominador = denominador * (xi[i] - xi[j])
      termino = (numerador/denominador) * yi[i]
    
    polinomio = polinomio + termino
  polisimple = sym.expand(polinomio) #Desarolla algebraicamente el polinomio
  #Salida
  print(f'\nEl polinomio NO desarollado es : \n\t {polinomio}')
  print(f'\n\nEl polinomio desarollado es : \n\t {polisimple}')

  return x, polinomio #Valores que necesitamos para graficar
  

x, polinomio = IntLagrange(xi, yi)


def graficaLagrange(xi,yi,x,polinomio,muestras):
  px=sym.lambdify(x,polinomio)
  n=len(xi)
  a=xi[0]
  b=xi[n-1]
  pxi=np.linspace(a,b,muestras)
  pyi=px(pxi) #Evalua la funcion 
  #Graficar
  plt.plot(xi,yi,'o')
  plt.plot(pxi,pyi)
  plt.show()
  return px

muestras=20
px=graficaLagrange(xi,yi,x,polinomio,muestras)
xmuestra=np.array([1/2,1/3,-1/4,1/5])
print("f(xm)=",  px(xmuestra))

