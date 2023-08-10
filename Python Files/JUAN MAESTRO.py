from ast import While
from pickle import TRUE


print("Bienvenido a la app Juan Maestro")

flag = True
print("Juan Maestro APP")
print("\t1.Registrar Cliente\n\t2.Suscripcion\n\t3.Consultar Datos Clientes\n\t4-Salir")
opcion=int(input("ingrese opciones disponibles: "))
while flag:
    if opcion == 1 :

        print("Registre sus datos")
        nombre=input("ingrese nombre: ")
        while True:
            try:
                rut=input("ingrese rut: ")
                #validacion de cedula
                while int(rut) not in range(4000000,999999999):
                    print("ingrese digito valido")
                    rut=input("ingrese rut: ")
            except:
                print("ingrese solo numeros")
            else:
                break

        edad=input("ingrese edad: ")
        while int(edad) not in range(0,110):
            print("ingrese edad valida")
            edad=input("ingrese edad: ")
        direccion=input("ingrese direccion: ")
        comuna=input("ingrese comuna: ")
        genero=input("ingrese genero: ")
        correo=input("ingrese Correo electronico: ")
        celular=input("ingrese su numero de telefono: ")
        print("gracias por registrarse en juan maestro")
    elif opcion == 2:
        #Suscripcion
        pass
    elif opcion == 3:
        #Consultar Datos
        pass
    elif opcion == 4:
        flag = False
        print("¡vuelva pronto!")
    else:
        print("elige una opcion valida")
        opcion=int(input("ingrese opcion disponible: "))

