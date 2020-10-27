import numpy as np

print('Metodo de Gauss Sidel')


def gs( A, b, tol ): # Gauss Sidel
  A= np.array(A, dtype = np.float32) # Evita problemas en la aproximacion
  b= np.array(b, dtype = np.float32) # Evita problemas en la aproximacion
  it=0
  n = len(A[:]) #El largo de toda la matriz (Al ser cuadrada , con el tamañi del renglon jala xd)
  x = np.zeros((n)) #Crea una matriz cuadrara de zeros
  
  while True:
    xi = x[0]
    
    for i in range(n):
      pivote = A[i, i]
      for j in range(n): #Se normaliza la matriz por renglones j 
        A[i, j] = A[i, j] /pivote #Esto es similar al coeficiente que divide el renglon a mano
      
      b[i] = b[i] /pivote  #Divide al termino independiente del renglon 
    
    
    for i in range(n): #Calculando el valor de x
      sum = b[i]
      for j in range(n):
        if(i != j): #Sirve al ser una matriz cuadrara
          sum = sum- A[i, j] * x[j]
      x[i] = sum
    
    Ea = np.abs(xi - x[0])
    print(f'x = {x}')
    print(f'Ea = {Ea}')
    print(f'Iteracion {it} , tolerancia {tol}')
    it += 1
    if( Ea < tol):
      break


A = np.matrix([[3, 1, 1], [2, 3, -1], [1, -1, 4]])
b = np.matrix([[19], [18], [6] ])
tol = 0.1
#gs(A, b, tol)

#COMPROBACION
x = np.matrix([ [5.078], [2.922], [0.9609] ])
print(f'b = {A*x}')