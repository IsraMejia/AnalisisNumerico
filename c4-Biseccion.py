import numpy as np
import matplotlib.pyplot as plt

print('\n\t Metodo de Biseccion \n')

x = np.arange(0,2, 0.1) #Rango de 0 a 2 con incrementos de 0.1
#print(x) #Lista de valores que puede tener x

def f(x):
    return np.power(x,2) - 2

tolerancia = 0.1

#Puntos del intervalo a evaluar
a = 1.25 
b = 1.5

print(f'El punfo f(a) = {f(a)} ') # f'El punfo f(a) = {f(a)} ' 
print(f'El punfo f(b) = {f(b)} ')

#Buscando el punto medio
c= (a+b) /2
print(c)
print(f'El punfo f(c) = {f(c)} ')

Ea = abs(a - b)
print(f'Error absoluto {Ea}')


plt.plot(x , f(x) )
ax = plt.gca() #Captar atributos
ax.tick_params(axis = 'x' , colors = 'red') #Dibuja el eje x con rojo
ax.tick_params(axis = 'y' , colors = 'blue') #Dibuja el eje y con azul
ax.spines['bottom'].set_position(('data' , 0)) #recta x=0
plt.grid(bool) #Cuadricula
plt.show() #Muestra la ventana de la grafica