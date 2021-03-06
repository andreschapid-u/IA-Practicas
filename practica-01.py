# -*- coding: utf-8 -*-
# practica-01.py
# Inteligencia Artificial, tercer curso del Grado de Ingeniería Informática -
# Tecnologías Informáticas. Universidad de Sevilla.

# Práctica 1: Introducción a Python
# =================================

# En esta práctica veremos algunos ejercicios de Python, para ir
# familiarizándonos con el lenguaje.


# -----------
# EJERCICIO 1
# -----------
#
# Escribir una función cuadrados(l) que recibiendo una secuencia l de números,
# devuelve la lista de los cuadrados de esos números, en el mismo orden.


# Por ejemplo:
# 
# >>> cuadrados([4,1,5.2,3,8])
# [16, 1, 27.040000000000003, 9, 64]

# Hacer dos versiones: una usando un bucle explícito, y la otra mediante
# definición de listas por comprensión.
# ---------------------------------------------------------------------------

# Por comprensión:

def cuadrados1(l):
    a = [ a*a for a in l ]
    return a

# Usando bucle:

def cuadrados2(l):
    a = []
    for i in l:
        a.append(i*i)
    return a


# -----------
# EJERCICIO 2
# -----------
# Definir una función vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayúsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------

def vocales_consonantes(s):
    vocales = "AEIOU"
    for i in s:
        if vocales.find(i)==-1:
            print('{0} es consonante'.format(i))
        else:
            print('{0} es vocal'.format(i))                


# -----------
# EJERCICIO 3
# -----------

# Usando como técnica principal la definición de secuencias por comprensión,
# definir las siguientes funciones:

# a) Dada una lista de números naturales, la suma de los cuadrados de los
#    números pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120

def suma_cuadrados(l):
    t=0
    for i in l:
        if i % 2 == 0:
            t += i*i        
    return t

# b) Dada una lista de números l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_fórmula([2,4,6,8,10])
# 110


def suma_formula(l):
    n = len(l)
    t = 0
    l1 = [(i+1)*l[i] for i in range(n)]
    for k in l1:
        t+=k
    return t

# c) Dadas dos listas numéricas de la misma longitud representando dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos. 

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def sqrt(n):
    return n**(1/2.0)

def distancia(l1,l2):
    n  = len(l1)
    l3 = [(l1[i]-l2[i])**2 for i in range(n)]
    t = 0
    for i in range(n):
        t+=l3[i]
    return sqrt(t)

# d) Dada una lista y una función de un argumento, devolver la lista de los
#    resultados de aplicar la función a cada elelemnto de la lista.

# Ejemplo:

# >>> map_mio(abs,[-2,-3,-4,-1])
# [2, 3, 4, 1]

def map_mio(f,l):
    l1 = [ f(a) for a in l]
    return l1

# e) Dada un par de listas (de la misma longitud) y una función de dos
#    argumentos, devolver la lista de los resultados de aplicar la función a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.


# Ejemplo:

# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio(f,l1,l2):
    l3 = [f(l1[i],l2[i]) for i in range(len(l1))]
    return l3

# f) Dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero. 

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(l):
    n = len(l)
    l1 = [ 1 for i in range(n) if (l[i] % 3 == 0 and l[i] != 0)]
    return sum(l1)
#   return l1.len()

# f) Dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.  

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3


def cuenta_coincidentes(l1,l2):
    n = len(l1)
    t = sum([ 1 for i in range(n) if l1[i] == l2[i] ])
    return t

# g) Dadas dos listas de la misma longitud, devolver un diccionario que tiene
# como claves las posiciones  en las que coinciden los elementos de ambas
# listas, y como valor de esas claves, el elemento coincidente. 

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(l1,l2):
    n = len(l1)
    l3 = {i:l1[i] for i in range(n) if l1[i]==l2[i]}
    return l3

# -----------
# EJERCICIO 4
# -----------
# Un número es perfecto si es la suma de todos sus divisores (excepto él
# mismo). Definir una función filtra_perfectos(n,m,p) que imprime por pantalla
# todos los números perfectos entre n y m que cumplen la condición p. Se pide
# también que se indiquen los divisores de cada número perfecto que se
# imprima. 

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------

def divisores(n):
    divs = [ i for i in range(1,n) if n%i == 0]
    return divs

def filtra_perfectos(n,m,p):
    l1 = [a for a in range(n,m) if p(a)== True and sum(divisores(a)) == a]
    for i in l1:
        print("El {0} es perfecto y sus divisores son {1}".format(i,divisores(i)))



# -----------
# EJERCICIO 5
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros 
# entre 0 y 50. 
# Definir una función histograma_horizontal(d), que recibiendo un diccionario 
# de ese tipo, escribe un histograma de barras horizontales asociado, 
# como se ilustra en el siguiente ejemplo:  

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------

def representacion(n):
    i = 0
    while i<n:
        print("*"),
        i+=1
 

def histograma_horizontal(d):
    l1 = sorted(d.keys())
    n  = len(l1)        
    for i in l1:
        print("{0} :".format(i)),
        representacion(d[i])
        print("")
    return

# -----------
# EJERCICIO 6
# -----------
# Con la misma entrada que el ejercicio anterior, definir una función
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical. 

# Ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *         
#           *         
#           *         
#           *         
#           *         
#         * * *       
#         * * *       
#         * * *       
#       * * * *       
#       * * * *       
#       * * * *       
#     * * * * * *     
#     * * * * * *     
#   * * * * * * * *   
#   * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * * * 
# * * * * * * * * * * 
# a b c d e f g h i j

# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------




# -----------
# EJERCICIO 7
# -----------
#
#  
#  (a) Definir la función compresion(l) que devuelva la lista resultante de
#  comprimir la lista l que recibe como entrada, en el siguiente sentido: 
#  * Si el elemento x aparece n (n > 1) veces de manera consecutiva en l
#    sustituimos esas n ocurrencias por la tupla (n, x)
#  * Si el elemento x es distinto de sus vecinos, entonces lo dejamos
#    igual
#  Ejemplo:
 
#  >>> compresión([1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8])
#  [[3, 1], 2, 1, 3, 2, [2, 4], 6, [3, 8]]
#  >>> compresión(["a", "a", "a", "b", "a", "c", "b", "d", "d", "f", "h", "h", "h"])
#  [[3, 'a'], 'b', 'a', 'c', 'b', [2, 'd'], 'f', [3, 'h']]

def compresion(l):
    n= len(l)
    xs = []
    t=1
    for i in range(n):
        if len(l)>1:
            if l[0] == l[1]:
                t += 1
                l.remove(l[0])
            else:
                if t > 1:
                    xs.append([t,l[0]])
                    l.remove(l[0])
                    t=1
                else:
                    xs.append(l[0])
                    l.remove(l[0])
        else:
            if t > 1:
                xs.append([t,l[0]])
            else:
                xs.append(l[0])
    return xs
                   
                
#  
#  (b) Definir la función descompresión(l) que devuelva la lista l descomprimida,
#  suponiendo que ha sido comprimida con el método del apartado anterior.
#  Ejemplo:

#  >>> descompresión([[3, 1], 2, 1, 3, 2, [2, 4], 6, [3, 8]])
#  [1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8]
# ************************************************************************

def descompresion(l):
    n = len(l)
    xs = []
    for i in range(n):
        if type(l[i]) is list:
            for k in range(l[i][0]):
                xs.append(l[i][1])
        else:
            xs.append(l[i])
    return xs


# -----------
# EJERCICIO 8
# -----------
#
# La profundidad de una lista anidada es el número máximo de anidamientos en
# la lista. Definir una función profundidad(l) que calcula la profundidad de
# una lista dada.

# Ejemplos:

# >>> profundidad(3)
# 0
# >>> profundidad([7,5,9,5,6])
# 1
# >>> profundidad([1,[1,[1,[1,1],1],[1,1]],1])
# 4

# Indicación: para saber si un dato es una lista, puede que sea útil la
# función "isinstance". En concreto, "isinstance(x,list)" comprueba si x es
# una lista.
# -------------------------------------------------------------------------
 
def profundidad(l):
    t= 0
    if isinstance(l,list):
        t = 1 + max([profundidad(l[i]) for i in range(len(l))])
        return t
    else:
        return t


# -----------
# EJERCICIO 9
# -----------
#
# Definir la función pertenece_prof(x,l), que comprueba la pertenencia de x a
# una lista l anidada
# 
# Ejemplos:

# >>> pertenece_prof(1,[2,[3,[4,[1]]]])
# True
# >>> pertenece_prof("a",[["c",["d","e",["f","a"],"g"],"h"],["i",["j","k"],"l"],"b",["x","y"]])
# True
# >>> pertenece_prof("a",[["c",["d","e",["f","m"],"g"],"h"],["i",["j","k"],"l"],"b",["x","y"]])
# False
#
# Indicación: puede ser de utilidad la función "any" (consultar su
#    especificación el manual)
# -----------------------------------------------------------------------

def pertenece_prof(x,xs):
    if isinstance(xs,list):
        return any([pertenece_prof(x,xs[i]) for i in range(len(xs))])
    else:
        return (x == xs)



# ------------
# EJERCICIO 10
# ------------
# 
# Definir una función mi_grep(cadena,fichero) similar al comando grep de unix
# (sin uso de patrones). Es decir, escribe por pantalla las líneas de fichero
# en las que ocurre cadena (junto con el número de línea).

# Por ejemplo, si buscamos la cadena "función" en un fichero similar a éste,
# las prímeras líneas de la salida podría ser similar a esta: 

# >>> mi_grep("función","ejercicios.py")
#
# Línea 4: # Escribir una función cuadrados(l) que recibiendo una secuencia l de números,
#                         ^^^^^^^
# Línea 36: #  Definir la función compresion(l) que devuelva la lista resultante de
#                         ^^^^^^^
# Línea 50: #  Definir la función descompresion(l) que devuelva la lista l descomprimida,
#                         ^^^^^^^
# Línea 121: # Definir una función vocales_consonantes(s), que reciba una cadena de
#                          ^^^^^^^
# Línea 155: # Definir una función oculta_palabras(s) que reciba una cadena de caracteres
#                          ^^^^^^^
# Línea 180: # Definir, sin usar "slicing", una función es_palíndromo(s) que reconoce si
#                                               ^^^^^^^
# ---------------------------------------------------------------------------

def mi_grep(st,fich):
    f=open(fich)
    t=0
    for line in f:
        t+=1
        if st in line:
            print("Línea {0}:".format(t)),
            print(line)


# ------------
# EJERCICIO 11
# ------------
# Supongamos que queremos simular la trayectoria de un proyectil que se
# dispara en un punto dado a una determinada altura inicial. El disparo se
# realiza hacia adelante con una velocidad inicial y con un determinado ángulo. Inicialmente
# el proyectial avanzará subiendo pero por la fuerza de la gravedad en un
# momento dado empezará a bajar hasta que aterrice. Por simplificar,
# supondremos que no existe rozamiento ni resistencia del viento.

# Diseñar una clase Proyectil que sirva representar el estado del proyectil en
# un instante de tiempo dado. Para ello, necesitamos al menos los siguientes
# atributos de datos:
# - Distancia recorrida (en horizontal)
# - Altura
# - Velocidad horizontal
# - Velocidad vertical

# Además, incluir los siguientes tres métodos:
# - actualiza(t): actualiza la posición y la velocidad del proyectil tras t
#   segundos
# - obtén_posx(): devuelve la distancia horizontal recorrida 
# - obtén_posy(): devuelve la distancia vertical recorrida 

# Una vez definida la clase Proyectil, usarla para definir una función 
#    aterriza(altura, velocidad, ángulo, intervalo)
# que imprimirá por pantalla las distintas posiciones por las que pasa un
# proyectil que se ha disparado con una velocidad, un ángulo (en grados) 
# y una áltura inicial dada. Se mostrará la posición del proyectil 
# en cada intervalo de tiempo, hasta que aterriza.
# Además se mostrará la altura máxima que ha alcanzado, cuántos intervalos de
# tiempo ha tardado en aterrizar y el alcance que ha tenido 

# Indicaciones:

# - Si el proyectil tiene una velocidad inicial v y se lanza con un ángulo
#   theta, las componentes horizontal y vertical de la velocidad inicial son
#   v*cos(theta) y v*sen(theta), respectivamente.
# - La componente horizontal de la velocidad, en ausencia de rozamiento 
#   y viento, podemos suponer que permanece constante.
# - La componente vertical de la velocidad cambia de la siguiente manera
#   tras un instante t: si vy0 es la velocidad vertical al inicio del
#   intervalo, entonces al final del intervalo tiene una velocidad 
#   vy1=vy0-9.8*t, debido a la gravedad de la tierra.
# - En ese caso, si el proyectil se encuentra a una altura h0, tras un
#   intervalo t de tiempo se encontrará a una altura h1=h0 - vm*t, donde vm 
#   es la media entre las anteriores vy0 y vy1. 
# - Será necesario importar la biblioteca "math"

# Ejemplo:

# >>> aterriza(30,45,20,0.01)
# Proyectil en posición(0.0,0.0)
# Proyectil en posición(0.4,0.2)
# Proyectil en posición(0.8,0.3)
# Proyectil en posición(1.3,0.5)
# Proyectil en posición(1.7,0.6)
# Proyectil en posición(2.1,0.8)
# Proyectil en posición(2.5,0.9)
# Proyectil en posición(3.0,1.1)
# Proyectil en posición(3.4,1.2)
#           ·······
# ·······SALIDA OMITIDA ·······
#           ·······
# Proyectil en posición(129.0,1.4)
# Proyectil en posición(129.4,1.2)
# Proyectil en posición(129.8,1.1)
# Proyectil en posición(130.2,0.9)
# Proyectil en posición(130.7,0.8)
# Proyectil en posición(131.1,0.6)
# Proyectil en posición(131.5,0.5)
# Proyectil en posición(131.9,0.3)
# Proyectil en posición(132.4,0.2)
# Proyectil en posición(132.8,0.0)
# 
# Tras 315 intervalos de 0.01 segundos (3.15 segundos) el proyectil ha aterrizado.
# Ha recorrido una distancia de 133.2 metros
# Ha alcanzado una altura máxima de 12.1 metros
# -----------------------------------------------------------------------------

import math


class proyectil:
    def __init__(self, alturaInic, vInic, angulo,ejeX):
        self.ejeX = ejeX
        self.altura = alturaInic
        self.vhor = vInic*math.cos(angulo)
        self.vver = vInic*math.sin(angulo)

    def actualiza(self,t):
        vInic = self.vver
        self.vver = vInic-9.8*t # Actualiza velocidad eje Y
        h0 = self.ejeX
        vh = self.vhor
        self.ejeX = h0 + vh*t # Actualiza posición eje X
        altInic = self.altura
        vm = (vInic+self.vver)/2
        self.altura = altInic + vm*t # Actualiza altura
        
    def obten_posX(self):
        return self.ejeX
    
    def obten_posY(self):
        return self.altura

def aterriza(altura, velocidad, angulo, intervalo):
    proy = proyectil(altura,velocidad, angulo,0)
    numInt = 0
    altMax = [0]
    while proy.obten_posY() >= 0:
        numInt += 1
        print("Proyectil en posición ({0},{1}) ".format(proy.obten_posX(),proy.obten_posY()))
        proy.actualiza(intervalo)
        altMax.append(proy.altura)
    alturaMax = max(altMax)    
    print("Tras {0} intervalos de {1} segundos ({2} segundos) el proyectil ha aterrizado.".format(numInt, intervalo, numInt*intervalo))
    print("Ha recorrido una distancia de {0} metros.".format(proy.obten_posX()))
    print("Ha alcanzado una altura máxima de {0} metros.".format(alturaMax))
       
       
