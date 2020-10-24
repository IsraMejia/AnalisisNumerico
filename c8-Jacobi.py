#Método de Jacobi
import numpy as np

def jacobi(A,b,tol):
  n=len(A[0:])
  #np.zeros   -- Crea una matriz con elementos = 0 , con su tamaño (n,n)
  Di=np.zeros((n,n))
  D=np.zeros((n,n))
  for i in range(n):
    D[i,i]=A[i,i]
  R=A-D
  for i in range(n):
    Di[i,i]=1/A[i,i]
  x=Di*b
  Dib=Di*b
  DiR=Di*R
  it=0
  while True:
    x1=Dib-DiR*x
    print("Iteración :",it)
    print("x=\n",x1)
    Ea=np.abs(x1-x)
    print("Ea=\n",Ea)
    it+=1
    cont=0
    for ea in Ea:
      if(ea < tol):
        cont+=1
    if( cont == n):
      print("Solución obtenida:\n ",x1)
      break
    else:
      x=x1


#Ingresando valores para calcular
A=np.matrix([[3,1,1],[2,3,-1],[1,-1,4]])
b=np.matrix([[19],[18],[6]])
jacobi(A,b,0.1)

#Comprobacion
#x=np.matrix([[4.949],[3.113],[1.047]])
#print("Ax=",A*x)