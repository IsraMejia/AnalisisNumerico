import numpy as np
import c12GaussJordan as gs
import c12MetLin as lin
#Metodo de Krylov

print('Metodo de Krylov')

A=np.matrix([[1,2,4],[7,3,1],[0,1,4]])
y=np.matrix([[1],[0],[0]])

print("A=\n",A)
print("y=\n",y)

def krylov(A, y):
  n = len(A[0:]) #La longitud de la matriz A iniciando en 0
  cont = n-1
  m = np. zeros((n,n))
  b = np.zeros((n,1))
  Ak = A*y # el producto de la matrices krylov
  m[0: , cont: ] = y #m se rellena con y en  A2

  while cont > 0 : 
    if(cont != 0):
      m[0: , 0:cont] = Ak
    print('A{0} = \n {1}'.format(cont, Ak))
    print('m = \n', m)
    Ak = A * Ak
    cont -= 1
  return m, -Ak

m, Ak = krylov(A, y)
  
print("b=\n", Ak)

b = gs.gaussJordan(m, Ak) #Se usa el metodo de gaus Jordan del archivo que se importa
print( b) 

b = [1, -8, 4, 17]
lin.Lin(b, 0.0001) #Se le manda b y su tolerancia

print('Raiz 1 es = \n', 7.009)
print()
