
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
    print("====== MENU CENTRO MEDICO DUOC ======")
    print("1.- Registrar Cliente")
    print("2.- Buscar Cliente")
    print("3.- Consultar Datos cliente")
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
        print(f"hasta luego, {nombre} version: 1,23030.")


#####################
#####################

    elif opcion == 1:
        try:
            NIF     = int(input("ingrese su NIF      : "))

            if NIF < 5000000 or NIF > 99999999:
                raise("El NIF no es válido")
        except:
            print("\n***** El NIF no es válido *****")
            input("Presione enter para continuar.....")
            continue


        nombre      = input("ingrese su nombre      : ")
        

        nacimiento   = input("ingrese su nacimiento   : ")


        estado = input("ingrese su estado conyugal (casado o soltero):")

        if estado != 'casado' and estado != 'soltero':
            print("\n***** El dato no es válido *****")
            input("Presione enter para continuar.....")
            continue 
       
        edad = int(input("ingrese su edad        : "))
        if edad <= 15 or edad > 110:
            print("\n***** La edad no es válida *****")
            input("Presione enter para continuar.....")
            continue 

        pertenece = input("ingrese si pertenece a la Unión Europea  (si o no):")

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
