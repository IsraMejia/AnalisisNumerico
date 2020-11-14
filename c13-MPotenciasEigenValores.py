import numpy as np
import numpy.linalg as alg

print('Metodo de las potencias MINIMO')

def eigPotMin(A, x, tol):
  it = 0
  Ain = alg.inv(A) #Se le asigna la inversa de A
  print(f'La inversa de A es = \n{Ain}' )
  lx = 0

  while True:
    it += 1
    m = Ain * x
    print(it, m, lx)
    mmax = m.max() #El elemento maximo
    mmin = m.min() #El elemento minimo
    if (abs(mmax) >= abs(mmin)):
      lx1 = 1/mmax #Lamda 1
    else : 
      lx1 = 1/mmin #Lamda
    
    x = lx1 * m #Obtenemos el vector caracteristico
    
    Ea = abs(lx1 - lx)

    if(Ea < tol):
      print('\n\nEl resultado usando el metodo de potencia minima es:')
      print('\n\tValor caracteristico minimo', lx1)
      print("\n")
      break
    else:
      lx = lx1

def eigPotMax(A, x, tol):
  m = A*x
  lx = m.max()
  m = (1/lx) * m #Tansformando la matriz 
  it = 0

  while True:
    it += 1
    m = A*m
    lx1 = m.max()
    m = (1/ lx1) * m
    Ea = abs(lx - lx1)
    print('Ea = ', Ea)
    print(it, m , lx)
    
    if(Ea < tol):
      print('\n\nEl resultado usando el metodo de potencia Maxima es:')
      print('\n\tValor caracteristico', lx1)
      print("\n")
      break
    else:
      lx = lx1 


A = np.matrix([[1,2], [7, 5]])
x = np.matrix([[1], [1]])
tol = 0.1
potenciaMaxima = eigPotMax(A, x, tol)
potenciaMinima = eigPotMin(A, x, tol)
