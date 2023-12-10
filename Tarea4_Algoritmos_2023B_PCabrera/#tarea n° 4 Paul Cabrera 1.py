#tarea n° 4 Paul Cabrera ejercicio1
print(">>>-- Bievenido al CARBONERO --<<<")
nombre=input("Introduzca su nombre: ").title()
cedula=str(input("Introduzca su cédula: "))
correo=input(("Intruduzca su correo: "))

print("Elejir un tipo de hamburguesa")
print("a. Simple")
print("b. Doble")
print("c. Triple")
tipo=str(input("Opción: ")).lower()

if tipo=="a":
    costo=1.5
    cantidad=int(input("Cuantas desea: "))
    print("Elejir forma de Pago")
    print("1. Tarjeta de crédito")
    print("2. Efectivo")
    pago=int((input("Opción: ")))

    if pago==1:
        forma="con Tarjeta de crédito"
    else:
        forma="en Efectivo"

    if pago==1:
        cargo=0.05
        total= cantidad*costo+((cantidad*costo)*cargo)
        print("Su pago es ", forma, "por favor cancelar: $ ", round(total,2))
        print(nombre, " Muchas gracias por su compra, vuelva pronto")
        print("Su factura será enviada al correo") 
    else: 
       if pago==2:
            cargo=0
            total= cantidad*costo+((cantidad*costo)*cargo)
            print("Su pago es ", forma, "por favor cancelar: $ ", round(total,2))
            print(nombre, " Muchas gracias por su compra, vuelva pronto")
            print("Su factura será enviada al correo") 
       else:
         print("El tipo de pago que ingreso no es válido")


else:
    if tipo=="b":
        costo=2.5
        cantidad=int(input("Cuantas desea: "))
        print("Elejir forma de Pago")
        print("1. Tarjeta de crédito")
        print("2. Efectivo")
        pago=int((input("Opción: ")))

        if pago==1:
            forma="con Tarjeta de crédito"
        else:
            forma="en Efectivo"

        if pago==1:
            cargo=0.05
            total= cantidad*costo+((cantidad*costo)*cargo)
            print("Su pago es ", forma, "por favor cancelar: $ ", round(total,2))
            print(nombre, " Muchas gracias por su compra, vuelva pronto")
            print("Su factura será enviada al correo") 
        
        else: 
           if pago==2:
                cargo=0
                total= cantidad*costo+((cantidad*costo)*cargo)
                print("Su pago es ", forma, "por favor cancelar: $ ",round(total,2))
                print(nombre, " Muchas gracias por su compra, vuelva pronto")
                print("Su factura será enviada al correo") 
        
           else:
                print("El tipo de pago que ingreso no es válido")
    else:
        if tipo=="c":
            costo=3.5
            cantidad=int(input("Cuantas desea: "))
            print("Elejir forma de Pago")
            print("1. Tarjeta de crédito")
            print("2. Efectivo")
            pago=int((input("Opción: ")))

            if pago==1:
               forma="con Tarjeta de crédito"
            else:
               forma="en Efectivo"

            if pago==1:
               cargo=0.05
               total= cantidad*costo+((cantidad*costo)*cargo)
               print("Su pago es ", forma, "por favor cancelar: $", round(total,2))
               print(nombre, " Muchas gracias por su compra, vuelva pronto")
               print("Su factura será enviada al correo") 
           
            else: 
                if pago==2:
                   cargo=0
                   total= cantidad*costo+((cantidad*costo)*cargo)
                   print("Su pago es ", forma, "por favor cancelar: ", round(total,2))
                   print(nombre, " Muchas gracias por su compra, vuelva pronto")
                   print("Su factura será enviada al correo") 
                else:
                    print("El tipo de pago que ingreso no es válido")
        else:
            print("Opción no valida")




