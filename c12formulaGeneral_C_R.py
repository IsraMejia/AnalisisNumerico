print('\n\nMejia Alba Israel Hipolito \t\t\tGrupo:07  - AnalisisNumerico')

print('\nEste programa calcula los resultados para raices Complejas y Reales')
# print('haciendo uso de la formula general.')
# print('Ingrese los correspondientes coeficientes de tu ecuacion ax^2 + bx + c\n')

# a = float(input('Coeficiente del termino cuadratico, a='))
# b = float(input('Coeficiente del termino lineal, b='))
# c = float(input('Coeficiente o termino independiente, c='))
# discri = raiz = x1 = x2 = 0.0


# while( a == 0 ):
#     a = float(input('Ingrese un valor Distinto a 0 del Coeficiente del termino cuadratico, a='))


def real(a, b, c , discri):
    raiz = ( discri )**(1/2)
    #print(f'raiz = {raiz}')
    x1 = ( -(b) + raiz ) / (2*a)
    x2 = ( -(b) - raiz ) / (2*a)
    print('\nLas raices obtenidas son las siguientes:')
    print('\n x1 = {:<8.4g} \t | \t x2 = {:<8.4g} \n'.format(x1, x2 ) )


def imaginario(a, b, c , discri):
    raiz = ( discri )**(1/2) #Ya se habia cambiado el signo previamente
    print(f'parteImaginaria = {raiz}')
    xr = (-(b)) / (2*a) #Parte real
    xi = raiz / (2*a) #Parte imaginaria
    print('\nLas raices obtenidas son las siguientes:')
    print('\n x1 = {:<8.4g} + {:<8.4g}i '.format(xr, xi ) )
    print('\n x2 = {:<8.4g} {:<8.4g}i \n'.format(xr, -xi ) )



def discriminante(a , b , c):
    discri =  (b**2) - 4*a*c 
    if( discri>0) :
        print(f'\nEl valor del discrimante es positivo (disc = {discri} ), tendremos resultado Real')
        return real(a, b, c, discri)
    else :
        print(f'\nEl valor del discrimante es negativo (disc = {discri} ), tendremos resultado Imaginario')
        discri = -1 * discri
        return imaginario(a, b, c , discri)

# discriminante (a , b , c)