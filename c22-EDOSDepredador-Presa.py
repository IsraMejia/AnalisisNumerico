#Método de Runge-Kutta de segundo orden 
#Para sistemas de ecuaciones de primer orden
import numpy as np
import matplotlib.pyplot as plt


#Condiciones inicales de Conejos y Linces
x0=2 #x1000 conejos
y0=1  #x1000 linces
h=0.5 #Años
tf=30  #Años
t0=0  #Años

#Ecuaciones diferenciales 
f= lambda t,x,y:0.5*x-0.7*x*y
g=lambda t,x,y:-0.35*y+0.35*x*y

# definiendo Método de Runge-Kutta de segundo Orden
def rk2s(x0,y0,t0,tf,h,f,g):
  a=t0 #Límite inferior
  b=tf #Límite superior
  n=int((b-a)/h)
  x=np.zeros(n+1)
  y=np.zeros(n+1)
  t=np.zeros(n+1)
  x[0]=x0
  y[0]=y0
  t[0]=t0
  for i in range(n):
    t[i+1]=t[i]+h 
  for i in range(n):
    k1=h*f(t[i],x[i],y[i])
    l1=h*g(t[i],x[i],y[i])
    k2=h*f(t[i+1],x[i]+k1,y[i]+l1)
    l2=h*g(t[i+1],x[i]+k1,y[i]+l1)
    x[i+1]=x[i]+0.5*(k1+k2)
    y[i+1]=y[i]+0.5*(l1+l2)
  return t,x,y


ts,xs,ys=rk2s(x0,y0,t0,tf,h,f,g)

plt.plot(ts,xs,label="Población de Conejos")
plt.plot(ts,ys,label="Población de Linces")
plt.legend()
plt.grid()
#plt.show()
print(ts)
print(xs)
print(ys)

