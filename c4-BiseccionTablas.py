import numpy as np
import matplotlib.pyplot as plt

print('\n\t Metodo de Biseccion \n')
print('\n Este es el codigo que compartio el profesor, que ya te imprime una tabla en consola :D\n')
print('Anexo lo suficiente para graficar')

x = np.arange(0 , 4 , 0.1) #Rango de 0 a 2 con incrementos de 0.1
#print(x) #Lista de valores que puede tener x

def f(x):
  return np.power(x,3)-x-1
a=1
b=3
it=1
tol=0.1
print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Itr','a','b','c','f(a)','f(b)','f(c)','Ea'))
while True:
  c=(a+b)/2
  fa=f(a)
  fb=f(b)
  fc=f(c)
  Ea=abs(a-b)    
  print ("{:<8} {:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g}".format(it,a,b,c,fa,fb,fc,Ea))  
  #g indica el número de cifras significativas
  it+=1
  if(Ea < tol):
    print("Raíz encontrada")
    print("{:0.4g}".format(c) ) #4cifras significativas
    break
  elif (fa*fc)<0:
    #El límite superior será c
    b=c
  elif (fb*fc)<0:
    #El límite inferior será c
    a=c
  else:
    print("No hubo cambio de signo, elija otro intervalo")
    a=float(input("Introduzca el límite inferior 'a':"))
    b=float(input("Introduzca el límite superior 'b: "))
    


plt.plot(x , f(x) )
ax = plt.gca() #Captar atributos
ax.tick_params(axis = 'x' , colors = 'red') #Dibuja el eje x con rojo
ax.tick_params(axis = 'y' , colors = 'blue') #Dibuja el eje y con azul
ax.spines['bottom'].set_position(('data' , 0)) #recta x=0
plt.grid(bool) #Cuadricula
plt.show() #Muestra la ventana de la grafica