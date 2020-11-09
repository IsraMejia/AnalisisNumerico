#Metodo Lin
import copy


#Polinomio
# a=[24,-26, 9, -1] #Coeficientes del polinomio
# tol=0.1

def Lin (a, tol):
  print('\n \t\tMetodo de Lin Bairstown - Factores Cuadraticos')
  p=0
  q=0
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
              if(k == n-2):
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

