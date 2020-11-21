import numpy as np 
import sympy as sym
import matplotlib.pyplot as plt


print('Interpolacion por diferencias Finitas progresivas')

xi = np.array([-2, -1, 0, 1, 2])   #Valores de X en la funcion
fi = np.array([-9, -2, -1, 0, 7])  #Valores de Y de la tabla


#-------------------------------Calculo de la tabla

n = len(xi) #Longitud de la tabla que haremos
ki = np.arange(0, n) #Indices de posiicon de la tabla
tabla = np.concatenate(([ki], [xi], [fi]), axis=0 ) #Ingresamos renglones
tabla = np.transpose(tabla)
# print(tabla) #Se acomoda la tabla como la vamos a utilizar
dfinita = np.zeros((n,n), dtype= float) #Matriz cuadrada de ceros del tamaño xi
tabla = np.concatenate((tabla, dfinita),  axis=1) #Se concatenan en columnas (forma vertical)
# print(tabla)
[n, m] = np.shape(tabla) #Dimensiones de la tabla n= renglones, m= columnas

#Calculando las primeras diferencias
j=3
i=0
diagonal = 0 #Que se genera en cada diferencia

while (j< m):
  i = diagonal
  while (i < n-1): #Para que no se desborde en los renglones
    tabla[i+1, j] = tabla[i+1, j-1]  -  tabla[i, j-1]
    i +=1
  diagonal +=1
  j+=1


print(tabla) #Cabeceras x,y, deltaY1, deltaY2, deltaY3, ... , deltaY6

#----------  Obteniendo el polinomio interpolante
x = sym.Symbol('x')
dfinita = np.array([7, -6, 6]) #Se toman las primeras 3 diferenias de la diagonal 
h = xi[1] - xi[0]
polinomio = fi[0]
n= len(dfinita)
k = (x-xi[0]) /h
termino = k 

for i in range( 1, n+1) : 
    polinomio = polinomio + termino*dfinita[i-1] /np.math.factorial(i)
    termino = termino * (k - i)

print(f'Polinomio normal = {polinomio}')

polinomiosimple = sym.expand(polinomio)
print(f'\nPolinomio desarrollado = {polinomiosimple}')
