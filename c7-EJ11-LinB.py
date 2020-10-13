#Metodo Lin
import copy
print('\n \t\tMetodo de Lin Bairstown - Factores Cuadraticos')
print('Cortesia de Diana Portillo, Alejandro Tapia e Ian Marentes que me ayudaron a recuperar el codigo')
print('\n\n\t Los resultados tabulados son:\n')
#Polinomio
a=[24,-26, 9, -1] #Coeficientes del polinomio
p=0
q=0

tol=0.1
b=copy.deepcopy(a) #Para poteger los valores de a
n=len(a) #Numero de elementos en a

while True:
    for k in range(n):
        if(k==0):
            b[k]=a[k]
        elif(k==1):
            b[k]=a[k]-p*b[k-1]
        else:
            b[k]=a[k]-p*b[k-1]-q*b[k-2]
            if(k==n-2):
                R=b[n-2]
                S=a[n-1]-q*b[n-3]
    dp=R/b[n-3]
    dq=S/b[n-3]
    b_format=["%8.4g" %elem for elem in b]
    print(b_format, "{:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g}".format(p,q,dp,dq))
    p=p+dp
    q=q+dq
    if(abs(R) < tol and abs(S) < tol):
        print("\n\n")
        break
print("\n Esto solo sirve para 3er grado")
print("p = {:<8.4g}  , q = {:<8.4g}".format(p,q))
print("b0 = {:<8.4g} , b1 = {:<8.4g}".format(b[0], b[1]))
print("\n Esto solo sirve para 3er grado, reescribir resultado y calcular raices\n")