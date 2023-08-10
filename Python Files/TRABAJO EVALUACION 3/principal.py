from funciones import *

clientes = []
opcion = menu()

while opcion != 4:
    if opcion == 1:
        grabar(clientes)
    elif opcion == 2:
        buscar(clientes)
    elif opcion == 3:
        imprimir_certificado(clientes)
    opcion = menu()
print("\n#####################################################")
print("¡Hasta pronto! Felipe Torres. Versión del programa: 1.0")
print("#####################################################")
