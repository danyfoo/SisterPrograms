__author__ = 'daniel'
from sympy import *

"""
    Ejemplo de uso de numeros racionales
"""
a = Rational(1,2)

print a

"""
    Ejemplo de uso de constantes numericas
"""

print pi**2
print pi.evalf()
print (pi+exp(1)).evalf()
print oo > 99
print oo + 1

#ejercicio

racional_a = Rational(1,2)

racional_b = Rational(1,3)

print racional_a + racional_b

"""
    Ejemplo de Uso de Variables
"""
x = Symbol('x')
y = Symbol('y')

print x+y+x-y
print (x+y)**2

#EXPANSION DE EXPRESION

print expand((x+y)**3)
print expand(x+y, complex=True)
print expand(cos(x+y), trig=True)

#SIMPLIFICACION DE EXPRESION

print simplify((x+x*y)/x)

#ejercicio

#calcular forma expandida de (x + y)**6

print expand((x+y)**6)
trig_expression = sin(x)/cos(x)

print simplify(trig_expression)