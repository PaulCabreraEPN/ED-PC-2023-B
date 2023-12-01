

nombre = input("Ingrese su nombre:")
apellido1 = input("Ingrese su primer apellido:")
apellido2 = input("Ingrese su segundo apellido:")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

inicial = inicial.upper()
print("Las iniciales son:",inicial)
