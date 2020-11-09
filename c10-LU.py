#Método LU
import numpy as np

print('Metodo de LU')
         

def descLU(A,b):
  A=np.array(A,dtype=np.float32)
  b=np.array(b,dtype=np.float32)
  print("A=\n",A)
  print("b=\n",b)
  m=len(b)#tamño de la matriz b
  x=np.zeros([m,1])
  y=np.zeros([m,1])
  #Matriz U
  U=np.zeros([m,m])#Matriz U
  #Matriz L
  L=np.identity(m)#L es matriz identidad cuadrada m
  
  for i in range(m):
    for j in range(i+1,m):
      factor=(A[j,i]/A[i,i])#Se divide entre los factores de la matriz diagonal
      L[j,i]=factor
      for c in range(m):
        A[j,c]=A[j,c]-factor*A[i,c] #Recorriendo las columnas y operando la transformacion
  
  #Obteniendo la solución para y
  y[0]=b[0]  
  for i in range(1,m): #Sustituyendo valores obtenidos
    suma=0
    for j in range(m):
      suma=suma+L[i,j]*y[j]
    y[i]=b[i]-suma #Sustitucion para obtener a "y"

  U=A
  x[m-1]=y[m-1]/U[m-1,m-1]
  for i in range(m-2,-1,-1):   #Empieza en el ultimo indice y va de reversa
    suma=0
    for j in range(m):
      suma=suma+U[i,j]*x[j]
    x[i]=(y[i]-suma)/U[i,i] #Despejando valores obtenidos
  
  return L,U,y,x

#Ingresar sin numpy
A=np.matrix([[-1,3,2],[3,-4,1],[2,5,-2]])
b=np.matrix([[10],[20],[22]])

L,U,y,x=descLU(A,b) #Asignamos resultados
print("L=\n",L)
print("U=\n",U)
print("y=\n",y)
print("x=\n",x)
print("Comprobación A*x=\n",A*x)    