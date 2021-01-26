#Runge-Kutta de segundo orden para sistemas de ecuaciones
#Forma matricial
import numpy as np
import matplotlib.pyplot as plt

#Condiciones iniciales
t0=0 #tiempo inial
h=0.1 # cada 0.1 seg
tf=10 #tiempo final
x0=np.array([0,2]) #Inicial y velocidad inicial?

#Ecuación diferencial
f=lambda t,x: np.array([x[1],-9.81*np.sin(x[0])])


def srk2(x0,t0,tf,h,f):
  a=t0 #Límite inferior
  b=tf #Límite superior
  n=int((b-a)/h) #Número de intervalos  
  t=np.zeros(n+1)
  nueq=len(x0) #numero de ecuaciones
  x=np.zeros((n+1,nueq)) #Primer columna desplazamiento, segunda de la velocidad
  x[0,:]=x0 #El primer renglon es de las condiciones inciales
  
  for i in range(n):
    t[i+1]=t[i]+h
  for i in range(n):
    k1=h*f(t,x[i,:])
#    print(k1)
    k2=h*f(t[i+1],x[i,:]+k1)
#    print(k2)
    #print(k1+k2)
    x[i+1,:]=x[i,:]+0.5*(k1+k2)
  return t,x

ts,xs=srk2(x0,t0,tf,h,f)

plt.plot(ts,xs[:,1],label="Velocidad Angular")
#plt.plot(ts,xs[:,0],label="Desplazamiento Angular")
plt.grid()
plt.show()




