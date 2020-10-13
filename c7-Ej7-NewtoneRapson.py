import numpy as np

print('\n\t\tNewton Rapson \n')

#Funcion original
def f(x):
  return 10* np.sin(x* np.exp(-x)) - 1

#Derivada de la funcion
def df(x):
  return 10* np.cos(x* np.exp(-x)) * (np.exp(-x) - x*np.exp(-x))


xi = .3 #Punto Inicial
tol = 0.00001
it=1
cabecera= "{:<8} {:<8} {:<8} {:<8}".format('Itera', 'x_i', 'x_i+1', 'Eabs')
print(cabecera)

while True:
    if( df(xi) == 0 ):
        xi = float(input('La derivada en evaluada en este punto es 0 \n Ingrese otro punto:'))
        continue
    
    xi1 = xi- (f(xi)/df(xi))
    Ea = abs(xi1 - xi)
    fila= "{:<8} {:<8.4g} {:<8.4g} {:<8.4g} ".format(it, xi, xi1, Ea)
    print(fila)
    xi = xi1
    it+=1
    
    if ( Ea < tol ):
        print("Raiz encontrada:")
        print("{:<8.4g}".format(xi1) )
        break
    
    
    
