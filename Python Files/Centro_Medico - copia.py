Pacientes = []
rut = ""
nombre = ""
direccion = ""
Prevision_Social = ""
correo = ""
edad = 0
genero = ""
Registros = ""

opcion = 0

while opcion != 4:
    print("====== MENU CENTRO MEDICO DUOC ======")
    print("1.- Registrar Paciente")
    print("2.- Atencion Paciente")
    print("3.- Consultar Datos Paciente")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese un opción: "))
    except:
        print("\n***** Opción ingresada no es válida *****")
        input("Presione enter para continuar.....")
        continue

    if opcion < 1 or opcion > 4:
        print("\n***** Opción ingresada no existe *****")
        input("Presione enter para continuar.....")
        continue

    if opcion == 4:
        print("Gracias por preferirnos <3")
    elif opcion == 1:
        try:
            rut         = int(input("ingrese su rut         : "))

            if rut < 5000000 or rut > 99999999:
                raise("El rut no es válido")
        except:
            print("\n***** El rut no es válido *****")
            input("Presione enter para continuar.....")
            continue

        nombre      = input("ingrese su nombre      : ")
        direccion   = input("ingrese su direccion   : ")
        correo      = input("ingrese su correo      : ")
        
        if correo.count("@") != 1:
            print("\n***** El correo no es válido *****")
            input("Presione enter para continuar.....")
            continue 
        
        
        edad = int(input("ingrese su edad        : "))
        if edad < 0 or edad > 110:
            print("\n***** La edad no es válida *****")
            input("Presione enter para continuar.....")
            continue 

        genero = input("ingrese su genero(F o M):")
        genero = genero.upper()
        if genero != 'F' and genero != 'M':
            print("\n***** El género no es válido *****")
            input("Presione enter para continuar.....")
            continue 
        


        celular     = input("ingrese su celular     : ")
        Prevision_Social       = input("ingrese su tipo: 1.-ISAPRE 2.-FONASA:").upper()
        if Prevision_Social != 'ISAPRE' and Prevision_Social != 'FONASA':
            print("\n***** La Prevision social no es valida *****")
            input("Presione enter para continuar.....")
            continue 

        fila = [rut, nombre, direccion, Prevision_Social, correo, edad, genero, celular, Registros]
        Pacientes.append(fila)
    
    elif opcion == 2:
        try:
            rut = int(input("ingrese su rut : "))

            if rut < 5000000 or rut > 99999999:
                raise("El rut no es válido")
        except:
            print("\n***** El rut no es válido *****")
            input("Presione enter para continuar.....")
            continue
        
        fueEncontrado = False
        for Paciente in Pacientes:
            if Paciente[0]==rut:
                fueEncontrado = True
                fecha=input("ingrese la fecha de registro:DD/MM/AA ")
                observaciones=input("ingrese obvservacion: ")
                Paciente[8]= fecha , observaciones
                print("Rut encontrado. Fecha agregada")
                input("Presione enter para continuar.....")
                break
        
        if not fueEncontrado:
            print("Rut no encontrado")

    elif opcion == 3:
        try:
            rut = int(input("ingrese su rut : "))

            if rut < 5000000 or rut > 99999999:
                raise("El rut no es válido")
        except:
            print("\n***** El rut no es válido *****")
            input("Presione enter para continuar.....")
            continue
        
        Pacienteregistrado = []
        for Paciente in Pacientes:
            if Paciente[0]==rut:
                Pacienteregistrado =  Paciente
                break
        
        if len(Pacienteregistrado) != 0:
            print("\n==== Datos del usuario encontrado ====")
            print("Rut              :", Pacienteregistrado[0])
            print("Nombre           :", Pacienteregistrado[1])
            print("Dirección        :", Pacienteregistrado[2])
            print("Prevision social :", Pacienteregistrado[3])
            print("Correo           :", Pacienteregistrado[4])
            print("Edad             :", Pacienteregistrado[5])
            print("Genero           :", Pacienteregistrado[6])
            print("Celular          :", Pacienteregistrado[7])
            print("Fecha Registro:  :", Pacienteregistrado[8])
            