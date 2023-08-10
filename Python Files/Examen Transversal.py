from datetime import date, datetime
import numpy as np 


entrada = np.array([["","","","","","","","","","","","","","","","","","","",""],
                 ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
                 ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",
                  "","","","","","","","","","","","","","","","","","","",""]],dtype=object)


def VentaEntrada(entrada):
    print("*** Compra de Entradas ****")
    print("Precios Disponibles")
    print("1.- Platinum $ 1200000") 
    print("2.- Gold $ 80000")
    print("3.- Silver $ 50000")

    try:
        opcion = int(input("Seleccione opción: "))
        if opcion not in [1,2,3]:
            print("La opción no es válida")
            input("Presione enter para continuar...")
            return

        fila = opcion - 1 
        mostrarColumnasDisponibles(entrada, fila)
        nroEntrada = int(input("ingrese número de entrada: "))
        columna = nroEntrada - 1 
        nombre = input("Ingrese nombre del cliente: ")
        while nombre.isnumeric():
            print("nombre invalido , use solo letras.")
            nombre = input("Ingrese nombre del cliente: ")
            
        while True:
            try:
                rut = int(input("Ingrese su rut:  "))
            except:
                print("solamente se aceptan digitos")  
            else:
                break
        entrada[fila][columna] = nombre,rut
        print(entrada)
        
       
    except:        
        print("Error en el ingreso de la opción")
        input("Presione enter para continuar...")
        return


def mostrarColumnasDisponibles(entrada, fila):
    nroEntrada = 1
    print("Entradas disponible de la fila: ", fila+1)
    for columna in entrada[fila]:
        if columna == "":
            print("Entrada nro:", nroEntrada)
        nroEntrada += 1


def mostrarUbicaciones(entrada):
    nroEntrada = 1
    valor = ""
    listado = ""
    print("Entradas disponibles")
    for fila in entrada: 
        for columna in fila:
            if columna == "":
                valor = str(nroEntrada)
            else:
                valor = "X"
            listado += valor + " "
            nroEntrada += 1
        listado += "\n"
    print(listado)
    input("Presione enter para continuar...")

def verListadoAsistentes(entrada):
    print("Asistentes Del Concierto")
    nroEntrada = 1
    for fila in entrada:
        for columna in fila:
           
            print("Entrada nro:  ", nroEntrada, "nombre y  rut :", columna)
            nroEntrada += 1
    input("Presione enter para volver al menú...")
def mostrarGanancias(entrada):
    print("Ganancias")
    total = 0
    fil = 1
    for fila in entrada:
        for columna in fila:
            if columna != "":
                if fil == 1:
                    total += 1200000
                elif fil == 2:
                    total += 80000
                elif fil == 3:
                    total += 50000            
        fil += 1
    print("Total de ganancias:", total)
    input("Presione enter para volver al menú...")



opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
while opcion != "5":
    print(" *****  Venta de Entradas ******")
    print("1.- Comprar entradas")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Ver listado de Asistentes")
    print("4.- Mostrar ganancias")
    print("5.- Salir")
    opcion = input("Seleccione una  opción: ")

    if opcion not in listaDeOpciones:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
        continue
    if opcion == "5":
   

     print("Usted ha salido del sistema." ,date.today(),"Felipe Torres") 
    
    else:
        if opcion == "1":
            VentaEntrada(entrada)
        elif opcion == "2":
            mostrarUbicaciones(entrada)
        elif opcion == "3":
            verListadoAsistentes(entrada)
        elif opcion == "4":
            mostrarGanancias(entrada)