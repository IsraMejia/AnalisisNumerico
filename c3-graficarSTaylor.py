import numpy as np
import matplotlib.pyplot as plt
"""Recuerden instalar los paquetes, una manera facil es que en el IDE de Tony
vayan a la seccion de Herramientas->ManejadorDePaquetes, lo buscan e instalan"""

print('\n\tEstoy graficando la Serie de Taylor recibiendo sus terminos \n')

x=np.arange(0,4,0.1) #de 0 a 4 con incremento de 0.1
def p(x):
  return 1-np.power(x,2)/2+np.power(x,4)/24
  #numpy.power(x,2) potencia de x^2
fo=np.cos(x)

plt.plot(x,p(x),label='Función aproximada o P(x)' )
#grafica a p(x), varIndependiente=x , varDepentiente=p(x) 
plt.plot(x,fo,label='Función original f(x)')
#grafica a fo, varIndependiente=x , varDepentiente=fo 
plt.grid(bool) #Cuadricula en la grafica
plt.legend() #Dibuja las etiquetas definidas en plt.plot(....)
plt.show() #Muestra la ventana de la grafica
#Acercandonos a Pi el error va creciendo, como lo calculamos a mano en el ejercicio 2

print('Hasta luego :)')
