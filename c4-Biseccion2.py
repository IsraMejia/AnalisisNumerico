import numpy as np
import matplotlib.pyplot as plt

print('\n\t Metodo de Biseccion \n')

x = np.arange(0 , 4 , 0.1) #Rango de 0 a 2 con incrementos de 0.1
#print(x) #Lista de valores que puede tener x

def f(x):
    return np.power(x,3) - x -1

tolerancia = 0.1
a = 1
print(f' a = {a} ')
b = 3
print(f' b= {b} ')
i = 1


while True: 
    #Puntos del intervalo a evaluar
    print(f'\n\nt Estamos en la iteracion {i}')
    c= (a+b) /2
    print(f' c= {c} ')#punto medio
    fa = f(a)
    fb = f(b)
    fc = f(c)
    print(f'El punfo f(a) = {fa} ') # f'El punfo f(a) = {f(a)} ' 
    print(f'El punfo f(b) = {fb} ')
    print(f'El punfo f(c) = {fc} ')#punto medio
    
    Ea = abs(a - b)
    print(f'Error absoluto {Ea}')
    
    i += 1  #Guardar la iteracion
  
    
    if (Ea < tolerancia) : 
        print(f'\n\t La Raiz es = {c}')
        break
    
    elif (fa * fc  < 0) : # si no hubo cambio de signo
        b = c
    elif f(b * fb  <0) : 
        a = c
    else : #Si no hay ningun cambio de signo ->Mal intervalo
        print("No hubo cambio de signo, elija otro intervalo")
        a = float(input('Introduce un nuevo limite Inferior :'))
        b = float(input('Introduce un nuevo limite Superior :'))
    
    



plt.plot(x , f(x) )
ax = plt.gca() #Captar atributos
ax.tick_params(axis = 'x' , colors = 'red') #Dibuja el eje x con rojo
ax.tick_params(axis = 'y' , colors = 'blue') #Dibuja el eje y con azul
ax.spines['bottom'].set_position(('data' , 0)) #recta x=0
plt.grid(bool) #Cuadricula
plt.show() #Muestra la ventana de la grafica