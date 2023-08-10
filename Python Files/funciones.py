import random


def menu():
    print("====== Centro de Identificacion Fiscal España ======")
    print("1.- Grabar Información")
    print("2.- Buscar Información")
    print("3.- Imprimir Certificados")
    print("4.- Salir")

    try:
        opcion_menu = int(input("Ingrese una opción: "))
        return opcion_menu
    except:
        print("Ingrese una opción válida")


def grabar(registrados):
    NIF = input("Ingrese su NIF: ")
    while len(NIF) != 8 or NIF.isalpha():
        print("NIF INVALIDO")
        NIF = input("ingrese su NIF: ")

    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha() or not len(nombre) >= 8:
        print("Nombre minimo 8 caracteres")
        nombre = input("ingrese su nombre: ")

    while True:
        try:
            nacimiento = int(input("Ingrese su año de nacimiento(AAAA) : "))
        except:
            print("Año no válido")
        else:
            break
    edad = 2022 - nacimiento
    if edad < 15:
        print("Su edad debe ser mayor o igual a 15 años")
        input("Presione enter para continuar.....")
        return

    estado = input("Ingrese su estado conyugal (casado o soltero): ").lower()
    while estado != 'casado' and estado != 'soltero':
        print("***** El dato no es válido *****")
        estado = input("ingrese su estado conyugal (casado o soltero):").lower()

    pertenece = input("Ingrese si pertenece a la Unión Europea (si o no): ").lower()

    while pertenece != 'si' and pertenece != 'no':
        print("***** El dato no es válido *****")
        pertenece = input("Ingrese si pertenece a la Unión Europea (si o no): ").lower()

    miembro = [NIF, nombre, nacimiento, estado, edad, pertenece]
    registrados.append(miembro)


def buscar(registrados):
    NIF = input("ingrese su NIF: ")
    while len(NIF) != 8 or NIF.isalpha():
        print("NIF INVALIDO")
        NIF = input("ingrese su NIF: ")

    for miembro in registrados:
        if NIF == miembro[0]:
            print("NIF               :", miembro[0])
            print("Nombre            :", miembro[1])
            print("Año de nacimiento :", miembro[2])
            print("Estado conyugal   :", miembro[3])
            print("Edad              :", miembro[4])
            print(f"Usted {miembro[5].upper()} pertenece a la UE.")
            break
    else:
        print(" " + "x" * 5 + " [ Usuario no registrado ] " + "x" * 5)
    input("Presione enter para continuar.....")


def imprimir_certificado(registrados):
    NIF = input("Ingrese su NIF: ")
    while len(NIF) != 8 or NIF.isalpha():
        print("NIF INVALIDO")
        NIF = input("ingrese su NIF: ")

    clienteregistrado = []
    for cliente in registrados:
        if cliente[0] == NIF:
            clienteregistrado = cliente
            break

    if len(clienteregistrado) != 0:
        print("\tCERTIFICADOS")
        print("1. Año de nacimiento")
        print("2. Estado conyugal")
        print("3. Pertenencia a la Unión Europea")

        certificado = input("Seleccione un certificado: ")

        if certificado == "1":
            print(f"==== CERTIFICADO DE NACIMIENTO ===="
                  f"\nEL CIUDADANO/A {clienteregistrado[1].upper()}"
                  f"\nCON NIF {clienteregistrado[0]}"
                  f"\nNACIÓ EN EL AÑO {clienteregistrado[2]}"
                  f"\n====================================")
        elif certificado == "2":
            print(f"==== CERTIFICADO DE ESTADO CIVIL ===="
                  f"\nEL CIUDADANO/A {clienteregistrado[1].upper()}"
                  f"\nCON NIF {clienteregistrado[0]}"
                  f"\nPOSEE EL ESTADO DE {clienteregistrado[3].upper()}")
            print("====================================")
        elif certificado == "3":
            print(f"==== CERTIFICADO DE LA UNIÓN EUROPEA ===="
                  f"\nEL CIUDADANO/A {clienteregistrado[1].upper()}"
                  f"\nCON NIF {clienteregistrado[0]}"
                  f"\n{clienteregistrado[5].upper()} ES MIEMBRO DE LA UNIÓN EUROPEA")
            print("====================================")
        else:
            print("Opción no válida")
        valor = (random.randint(10, 100))
        print(f"El valor de la impresion es de €{valor}")
        input("Presione enter para continuar.....")
    else:
        print(" " + "x" * 5 + " [ Usuario no registrado ] " + "x" * 5)
        input("Presione enter para continuar.....")
