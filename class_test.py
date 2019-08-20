import  numpy  as np
import math

class  desv_estandar:
    """ Descripcion  del  bloque  """
    def __init__(self , name="e_desv_estandar_cf",in_sig =[np.float32],out_sig =[np.float32 ]):



        #  variables  externas
        self.contador = 0
        self.acum=0

    def  work(self , input_items , output_items):
        #  traduccion  a algo  que  podemos  manejar  mejor
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        
        a1 = in0[(0.5 < in0) & (in0 < 1.5) & (in1<0.5) & (in1>-0.5)]    #sección 
        b1 = in1[(0.5 < in0) & (in0 < 1.5) & (in1<0.5) & (in1>-0.5)]


        a1bar = np.sum(a1)/a1.shape[0]                        #media y varianza de
        a1var = np.sum((a1 - a1bar)**2)/(a1.shape[0]-1);      #los reales (a)
        b1bar = np.sum(a1)/a1.shape[0]                        
        b1var = np.sum((a1 - a1bar)**2)/(a1.shape[0]-1);
        datos_desv_estandar = np.sqrt(a1var + b1var)
        out0 = datos_desv_estandar
        return  out0
    


obj1 = desv_estandar()
m=2
r=1
n=20
fvar=.1
pi=math.pi
datos = np.round((m-1)*np.random.rand(r,n))  #datos aleatorios
angles = datos*2*pi/m                   #angluos correspondientes
mag = fvar*np.random.normal(0,1,n) + 1       #agregar ruido a magnitud de vector complejo
a = mag*np.cos(angles+fvar*np.random.normal(0,1,n))   #parte real con efecto de ruido
b = mag*np.sin(angles+fvar*np.random.normal(0,1,n))   #parte imaginaria

ro = obj1.work([a,b],[0.])
print(ro)






















##print(a)
##print(b)
##blaa = [a,b]
##som = [0.]
##print(blaa)
##in0 = blaa[0]
##print(in0)
##in1 = blaa[1]
##out0 = som[0]
##        
##a1 = in0[(0.5 < in0) & (in0 < 1.5) & (in1<0.5) & (in1>-0.5)]    #sección 
##b1 = in1[(0.5 < in0) & (in0 < 1.5) & (in1<0.5) & (in1>-0.5)]
##
##
##a1bar = np.sum(a1)/a1.shape[0]                        #media y varianza de
##a1var = np.sum((a1 - a1bar)**2)/(a1.shape[0]-1);      #los reales (a)
##b1bar = np.sum(a1)/a1.shape[0]                        
##b1var = np.sum((a1 - a1bar)**2)/(a1.shape[0]-1);
##datos_desv_estandar = np.sqrt(a1var + b1var)
##print(datos_desv_estandar)
##out0 = datos_desv_estandar
##print(out0)
##print(som[0])
