from math import cos

print("\n\n\t Serie de Taylor\n")
pi=3.1416
valorAproxlorRelativo=cos(pi)
valorAprox=1- ((pi)**2/2) +  ((pi)**4/24)
print("valorAproxlor real: ", valorAproxlorRelativo)
print("valorAproxlor aproximado: ",valorAprox)
Ea=abs(valorAproxlorRelativo-valorAprox)
Er=Ea/abs(valorAproxlorRelativo)
Erp=Er*100
print("Error absoluto: ",Ea)
print("Error relativo: ", Er)
print("Error relativo porcentual", Erp)