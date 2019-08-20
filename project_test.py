import numpy as np
import math
import matplotlib.pyplot as plt

n=150
fvar=0.1
m=4            #numero de niveles de señal
r=1            #numero de señales para comparar entre
pi = math.pi
e=math.e
lim=1.5

datos = np.round((m-1)*np.random.rand(r,n))           #datos con m niveles
a1bar = np.zeros(r)
a1var = np.zeros(r)
b1bar = np.zeros(r)
b1var = np.zeros(r)
datos_desv_estandar = np.zeros(r)
for i in range(0,r):
    angles = datos[i,:]*2*pi/m
    mag = fvar*np.random.normal(0,1,n) + 1                  #magnitud, se agrega 
    a = mag*np.cos(angles+fvar*np.random.normal(0,1,n))   #efecto de ruido
    b = mag*np.sin(angles+fvar*np.random.normal(0,1,n))   #parte real e imaginaria

    plt.plot(a,b,'ro')
    plt.axis([-lim,lim,-lim,lim])
    plt.show()

    a1 = a[(0.5 < a) & (a < 1.5) & (b<0.5) & (b>-0.5)]    #sección 
    b1 = b[(0.5 < a) & (a < 1.5) & (b<0.5) & (b>-0.5)]

    plt.plot(a1,b1,'ro')
    plt.axis([-lim,lim,-lim,lim])
    plt.show()

    a1bar[i] = np.sum(a1)/a1.shape[0]                        #media y varianza de
    a1var[i] = np.sum((a1 - a1bar[i])**2)/(a1.shape[0]-1);      #los reales (a)
    b1bar[i] = np.sum(a1)/a1.shape[0]                        
    b1var[i] = np.sum((a1 - a1bar[i])**2)/(a1.shape[0]-1);
    datos_desv_estandar[i] = np.sqrt(a1var[i] + b1var[i])
    print(b1var)
    print(a1var)
    print(datos_desv_estandar)


resultado = np.where(datos_desv_estandar == np.amin(datos_desv_estandar))
 

print('Mejor señal para muestra es la señal: ', resultado[0])
print('Datos de la señal: ', datos[resultado,:])


















