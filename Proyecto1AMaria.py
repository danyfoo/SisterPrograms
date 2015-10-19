__author__ = 'Maria Dolores Rivera Guzman'

from sympy import * #Importar la libreria Sympy
import itertools    #Importar libreria itertools para trabajar iterators

temperatura = [
    26.9,
    32.28,
    36.315,
    44.923,
    50.572,
    53.8,
    63.215,
    66.174,
    74.782,
    79.086,
    80.7,
    89.308,
    94.419,
    97.378,
    101.682,
    107.6,
    118.36,
    123.471,
    130.465,
    131.541,
    134.5,
    137.19,
    144.184,
    153.061,
    156.827,
    161.4,
    171.622,
    174.85,
    180.499,
    183.996,
    188.3,
    196.101,
    198.522,
    205.427,
    212.779,
    215.2,
    217.621,
    224.346,
    235.106]

resistencia = [
    137.54,
    142.83,
    165.048,
    283.544,
    322.212,
    370.3,
    398.866,
    417.91,
    436.954,
    442.244,
    444.36,
    458.114,
    471.868,
    508.898,
    527.942,
    529,
    564.972,
    630.568,
    670.772,
    726.846,
    740.6,
    772.34,
    825.24,
    882.372,
    921.518,
    931.04,
    942.678,
    986.056,
    1029.434,
    1056.942,
    1068.58,
    1085.508,
    1147.93,
    1238.918,
    1300.282,
    1322.5,
    1346.834,
    1361.646,
    1367.994]

m = Symbol('m') #Definimos incognita m que es la pendiente a encontrar
b = Symbol('b') #Definimos incognita b que es la ordenada al origen

aux = 0 #Resultado de la medicion
f = 0   #Sumatoria de todos los datos

#A continuacion ingresamos todos los datos de resistencia y temperatura (y,x) uno a uno a la ecuacion de la funcion
#que realizara los minimos cuadrados
for x,y,index in itertools.izip(resistencia,temperatura, range(1,len(resistencia)+1)):
    aux = (y - (m*x) - b)**2 #Se van ingresando todos los datos
    f+=aux
    if index<10:
        print 'd[',index,']:\t\t', expand(aux)
    else:
        print 'd[',index,']:\t', expand(aux)

print ('\n')*2, 'f = ', expand(f)

dm =  diff(f,m) #Derivada parcial de f con respecto a m

print 'd/dm = ' , dm

db = diff(f,b)  #Derivada parcial de f con respecto a b

print 'd/db = ' , db

print solve([dm,db] , [m,b])    #Resolvemos el sistema de ecuaciones