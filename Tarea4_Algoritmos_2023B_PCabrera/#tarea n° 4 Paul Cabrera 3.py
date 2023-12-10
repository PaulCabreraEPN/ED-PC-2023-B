#tarea n° 4 Paul Cabrera 3 ejercicio3
print(">>>--Calculadora--<<<")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Divisíon")
print("5. Potencia")
print("6. Módulo")
opcion=int(input("Opción: "))

val1=float(input("Ingrese valor 1: "))
val2=float(input("Ingrese valor 2: "))

match opcion:
    case 1:
        resultado= val1+val2
        operación= "Suma"
        print("El resultado de ", operación, "es = ", resultado)
    case 2:
        resultado= val1-val2
        operación= "Resta"
        print("El resultado de ", operación, "es = ", resultado)
    case 3:
        resultado= val1*val2
        operación= "Multiplicación"
        print("El resultado de ", operación, "es = ", resultado)
    case 4:
        if val2==0:
            print("No existe la división para 0")
        else:
            resultado= val1/val2
            operación= "División"
            print("El resultado de ", operación, "es = ", round(resultado,2))
    case 5:
        resultado= val1**val2
        operación= "Potencia"
        print("El resultado de ", operación, "es = ", resultado)
    case 6:
        if val2==0:
            print("No existe la división para 0")
        else:
            resultado= val1%val2
            operación= "Módulo"
            print("El resultado de ", operación, "es = ", resultado)


