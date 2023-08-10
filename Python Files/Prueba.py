
from pickle import TRUE
import random


#################


clientes = []
NIF = ""
nombre = ""
nacimiento = ""
estado  = ""
edad = 0
pertenece  = ""
#################
Registros = ""

opcion = 0

while opcion != 4:
    print("====== Centro de Identificacion Fiscal España ======")
    print("1.- Grabar Información")
    print("2.- Buscar Información")
    print("3.- Imprimir Certificados")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese un opción: "))
    except:
        print("\n***** Opción ingresada no es válida *****")
        input("Presione enter para continuar.....")
        continue

#####################
#####################


    if opcion < 1 or opcion > 4:
        print("\n***** Opción ingresada no existe *****")
        input("Presione enter para continuar.....")
        continue

#####################
#####################
    if opcion == 4:
        print(f"¡¡ Hasta pronto !!, {nombre} version: 1.0")


#####################
#####################
    elif opcion == 1:
        NIF = input("ingrese su NIF: ")
        while len(NIF) !=8 or NIF.isalpha() :
            print("NIF INVALIDO")
            NIF = input("ingrese su NIF: ")
            
        
        nombre = input("ingrese su nombre      : ")
        while not nombre.isalpha() or not len(nombre) >= 8 :
            print("Nombre minimo 8 caracteres")
            nombre = input("ingrese su nombre: ")
            
            
            
        while True:
            try:
                nacimiento = int(input("ingrese su año de nacimiento(AAAA) : "))
            except:
                print("Año no válido")
            else:
                break
        edad = 2022 - nacimiento
        if edad < 15 :
            print("su edad debe ser mayor o igual a 15 años")
            input("Presione enter para continuar.....")
            continue 
        
        
        estado = input("ingrese su estado conyugal (casado o soltero):").lower()
        
        while estado != 'casado' and estado != 'soltero':
            print("\n***** El dato no es válido *****")
            estado = input("ingrese su estado conyugal (casado o soltero):").lower()

        pertenece = input("ingrese si pertenece a la Unión Europea  (si o no):").lower()

        if pertenece != 'si' and pertenece != 'no':
            print("\n***** El dato no es válido *****")
            input("Presione enter para continuar.....")
            continue 

        fila = [NIF, nombre, nacimiento, estado, edad, pertenece]
        clientes.append(fila)
    
#####################
#####################
    
    elif opcion == 2:
        try:
            NIF = int(input("ingrese su NIF : "))

            if NIF < 5000000 or NIF > 99999999:
                raise("El NIF no es válido")
        except:
            print("\n***** El NIF no es válido *****")
            input("Presione enter para continuar.....")
            continue
        
        fueEncontrado = False
        for cliente in clientes:
            fueEncontrado = True
            print("Rut encontrado.")
            print(f"usted {pertenece} pertenece a la UE.")
            input("Presione enter para continuar.....")
            break


#####################
#####################        

    elif opcion == 3:
        try:
            NIF = int(input("ingrese su NIF : "))

            if NIF < 5000000 or NIF > 99999999:
                raise("El NIF no es válido")
        except:
            print("\n***** El NIF no es válido *****")
            input("Presione enter para continuar.....")
            continue
        
        clienteregistrado = []
        for cliente in clientes:
            if cliente[0]==NIF:
                clienteregistrado =  cliente
                break
        
        if len(clienteregistrado) != 0:
            print("\n====     Certificado Cliente      ====")
            print("su NIF              :", clienteregistrado[0])
            print("Nombre              :", clienteregistrado[1])
            print("fecha de nacimiento :", clienteregistrado[2])
            print("estado conyugal     :", clienteregistrado[3])
            print("su edad             :", clienteregistrado[4])
            print("pertenece a la UE   :", clienteregistrado[5])

            valor = (random.randint(10, 100))
            input("##########################################")
            print(f"el valor de la impresion es {valor}€")

            input("Presione enter para continuar.....")
