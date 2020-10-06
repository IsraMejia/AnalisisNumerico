#Importando las librerías
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-3,3,0.01)

def f(x): 
    return np.power(x,3)+3*np.power(x,2)-1

plt.plot(x,f(x))
plt.grid(bool)
plt.show()