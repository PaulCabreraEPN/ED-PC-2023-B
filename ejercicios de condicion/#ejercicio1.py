cadena=input("Ingrese una palabra: ")
resultado=cadena.isupper()
if resultado!=True:
    print("La palabra ingresada contiene al menos una letra mayúscula.")
else:
    print("La palabra ingresada no contiene letras mayúsculas.")