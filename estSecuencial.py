
#Ejercicio 1
print("hola clase, Paul Cabera")

#ejercicio 2
print("Programa de suma de dos números")
numeroUno = 8
numeroDos = 9
suma = numeroUno + numeroDos
print("Paul Cabrera. El resultado de la suma es:", suma)

#ejercicio 3
#string
mensaje =("Hola")
mensaje +=(" ")
mensaje +=("clase")
mensaje +=(" ")
mensaje +=("de")
mensaje +=(" ")
mensaje +=("Algoritmos")
mensaje +=(" ")
mensaje +=("Estructura ")
mensaje +=(" ")
mensaje +=("de")
mensaje +=(" ")
mensaje +=("Datos")
mensaje +=(" ")
mensaje +=("Paul")
mensaje +=(" ")
mensaje +=("Cabrera")

print(mensaje)

#ejercicio 4
print("Programa que imprime cadena de caracteres con +")
nombre = "Paul"
apellido = "Cabrera"
curso = "Segundo"
asignatura = "Algoritmos de datos"

print(nombre+" "+ apellido +" "+ curso +" " + asignatura)


#ejercicio 5
print("Paul Cabrera. Programa que busca caracteres dentro de una cadena de caracteres")

mensaje = "Hola clase de Algoritmos de estructueras de datos"
subcadena= mensaje.find("Algoritmos")
print(subcadena)

#ejercicio 6
print("Paul Cabrera. Programa que busca un rango de cadena de caracteres")

mensaje = "Hola clase de Algoritmos de estructueras de datos"
subcadena= mensaje[14:20]
print(subcadena)

#ejercicio 7

print("Paul Cabrera. Progrma a que compara igualdad")
mensajeUno=("Hola Clase de Algoritmos y Estructura de Datos")
mensajeDos=("Hola Clase de Algoritmos y Estructura de Datos")

print(mensajeUno==mensajeDos)

#ejercicio 8
print("Paul Cabrera. Programa de Operadores aritméticos")
x=7
y=2
suma= x+y
resta= x-y
producto= x+y
division= x/y
resto= x%y
cociente= x//y
potencia= x**y

print(suma,resta, producto, division, resto, cociente, potencia)

#ejercicio 9
print("Paul Cabrera, Programa de Orden de precencia")
#Exponente: **
#Negación: -
#Multiplicación, división, división entera, módulo : * / // %
#Suma, resta: + -
print(2**1/12)
print(2**(1/12))

#ejercicio 10
print("Paul Cabrera, Programa de Orden de precencia o prioridad")
x=5
y=2
z=x+3*y #el producto tiene prioridad sobre la suma
print(z)
z=(x+3)*y #los parentecis tienen prioridad
print(z)

#ejercicio 11
print("Paul Cabrera, Programa de Operadores Lógicos")
x= True
y= False

print(x or y)
print(x and y)
print(not x)

#ejercicio 12
print("Paul Cabrera, Programa de Operadores Relacionales")
x=9
y=1
print(x<y)
print(x>y)
print(x==y)


#ejercicio 13
print("Paul Cabrera, Programa de Operadores Lógicos de Comparación")
x=9
print( 1 < x and x < 20)
print( 1 < x < 20)

#ejercicio 14
print("Paul Cabrera, Programa de Operadores a nivel de bits")
x=2
y=7
print(x^y)
print(x|y)
print(x&y)
print(x>>1)
print(x<<1)
print(~x)

#ejercicio 15
print("Paul Cabrera, Programa de Operadores de Asignación")

x=(10)
x += 2
print(x)

x=10
x -= 2
print(x)

x=10
x *= 2
print(x)

x=10
x /= 2
print(x)

x=10
x %= 2
print(x)

x=10
x //= 2
print(x)

x=10
x **= 2
print(x)

x=10
x &= 2
print(x)

x=(10)
x |= 2
print(x)

x=(10)
x ^= 2
print(x)

x=(10)
x >>= 2
print(x)

x=(10)
x <<= 2
print(x)
