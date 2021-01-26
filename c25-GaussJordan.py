import numpy as np

print('Metodo de Gauss JORDAN')

def gaussJordan(A, b):
  A = np.array(A,  dtype = np.float32)
  b = np.array(b,  dtype = np.float32)
  m = len(b) 
  aux = np.zeros(m)
  
  for i in range(m):
    for j  in range(i+1, m): #Para calular el siguiente elemento
      factor = (A[j, i] / A[i, i])
      b[j] = b[j] - factor*b[i]
      for c in range(m):
        A[j, c] = A[j, c] - factor * A[i, c]
  
  aux[m-1] = b[m-1] / A[m-1, m-1]

  print(f'El resultado es aux : {aux}')
  print('Realizando sustitucion hacia atras:')

  for r in range(m-2, -1, -1) : #Empieza del ultimo al primero
    suma = 0
    
    for c in range(m):
      suma = suma + A[r,c] * aux[c]
    
    aux[r] = (b[r] - suma) / A[r, r]


  return aux 


A = np.matrix([[-2, 1.125, 0], [1, -2.125, 1.125], [0, 0.875, 2]])
b = np.matrix([[0], [0], [4500] ])

gauss = gaussJordan( A, b )

print(f'\n\n\tLa matriz de resultados es: \n {gauss}')

#COMPROBACION

#x = np.matrix([[-36], [-224], [196] ])
#print(f'\n\nLa matriz b es: \n {A*x}')



 