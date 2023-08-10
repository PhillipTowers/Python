# 1- definir las variables
subTotal = 0
descuento= 0
valor    = 0
total    = 0

# 2- solicitar los datos al usuario
print("******  Super Cine Duoc Plaza Oeste ********")
print("Pertenece a DUOC UC PO")
print("1.- SI")
print("2.- No")
esDeDuoc = input("Seleccione opción: ")

print("======= Tipo de Entrada =======")
print("1.- Estreno")
print("2.- Normal")
tipoEntrada = input("Seleccione opción: ")
cantidadEntrada = input("Ingrese cantidad de entradas: ")

print("======= Palomitas de Maíz =======")
print("1.- Pequeña")
print("2.- Mediana")
print("3.- Grande")
palomitas = input("Seleccione opción: ")
cantidadPalomitas = input("Ingrese cantidad de palomitas: ")


print("======= Bebidas =======")
print("1.- Pequeña")
print("2.- Mediana")
print("3.- Grande")
bebidas = input("Seleccione opción: ")
cantidadBebidas = input("Ingrese cantidad de bebidas: ")

# Procesar información
if tipoEntrada == "1":
    valor = 4800 
else:
    valor = 2900
    
subTotal = valor * int(cantidadEntrada)

if esDeDuoc == "1":
    descuento = subTotal * .3

if palomitas == "1":
    valor = 2500
elif palomitas == "2":
    valor = 4500
else:
    valor = 7800

subTotal = subTotal + valor * int(cantidadPalomitas)
if bebidas == "1":
    valor = 1000
elif bebidas == "2":
    valor = 1250
else:
    valor = 2000

subTotal = subTotal + valor * int(cantidadBebidas)
# mostrar resultado

print("----------- Total a pagar -----------")
print("Subtotal     : ", subTotal)
print("Descuento    : ", descuento)
print("Total a pagar: ", (subTotal - descuento))