"Este es el ejercicio 26"
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

lista_productos = productos.split(",")

print("Los productos en tu cesta son:")
for producto in lista_productos:
    print(producto.strip())