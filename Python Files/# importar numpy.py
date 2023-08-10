# importar numpy
import numpy as nu
asientos = nu.array([["","","","","",""], ["","","","","",""], ["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]], dtype=object)
# definir funciones
def arrendar(asientos):
    print("*** Comprar Asiento ****")
    print("Listado de Asientos")
    mostrarUbicaciones(asientos)
    print(" Asiento VIP $ 10000 - Asientos del 31 al 42")
    print(" Asiento normal $ 5000 - Asientos del 1 al 30")
    
    try:
        valor = 0
        asiento = int(input("Seleccione opción: "))
        if asiento in range(31,42) :
            valor = 10000
        elif asiento in range(1,30):
            valor = 5000
            
        else:
            print("La opción no es válida")
            input("Presione enter para continuar...")
            return

        nombrepasajero = input("Ingrese nombre del cliente: ")
        rutpasajero = input("Ingrese rut del cliente: ")
        bancopasajero = input("Ingrese banco del cliente: ")
        telefonopasajero = input("Ingrese telefono del cliente: ")
        
        print(asientos)
        
        if bancopasajero =="BancoDuoc":
            total = valor - valor * 0.15
        print("TOTAL: ",valor)
            
    except:        
        print("Error en el ingrese de la opción")
        input("Presione enter para continuar...")
        return


def mostrarUbicaciones(asientos):
    nroAsiento = 1
    valor = ""
    listado = ""
    print("Disponibilidad de Asientos")
    for fila in asientos: 
        for columna in fila:
            if columna == "":
                valor = str(nroAsiento)
            else:
                valor = "X"
            listado += valor + " "
            nroAsiento += 1
        listado += "\n"
    print(listado)
    input("Presione enter para continuar...")

def verListadoCliente(asientos):
    print("Clientes de los casilleros")
    listado = ""
    nroAsiento = 1
    for fila in asientos:
        for columna in fila:
 #           if columna != "":
            print("Asiento: ", nroAsiento, "nombre:", columna)
            nroAsiento += 1
    input("Presione enter para volver al menú...")
def mostrarGanancias(asientos):
    print("Ganancias")
    total = 0
    fila = 1
    for fila in asientos:
        for columna in fila:
            if columna != "":
                if fila == 1:
                    total += 10000
                elif fil == 2:
                    total += 5000
                elif fil == 3:
                    total += 2000            
        fil += 1
    print("Total de ganancias:", total)
    input("Presione enter para volver al menú...")


# iniciar programa
opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
while opcion != "5":
    print("====== Menú Principal Asientos ======")
    print("1.- arrendar")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Ver listado de clientes")
    print("4.- Mostrar ganancias")
    print("5.- Salir")
    opcion = input("ingrese opción:")

    if opcion not in listaDeOpciones:
        print("La opción no es válida")
        input("Presione enter para continuar...")
        continue
    if opcion == "5":
        print("Adiós...")
    else:
        if opcion == "1":
            arrendar(asientos)
        elif opcion == "2":
            mostrarUbicaciones(asientos)
        elif opcion == "3":
            verListadoCliente(asientos)
        elif opcion == "4":
            mostrarGanancias(asientos)