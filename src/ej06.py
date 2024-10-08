"Este es el ejercicio 6"
#Escribe un programa que pida el importe final de un artículo 
#y calcule e imprima por pantalla el IVA que se ha pagado y el importe 
#sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

X = float(input("introduzca el importe con IVA : "))
#x es el valor del artículo
Y = 10
#Y es tipo de IVA 
J = X / (1 + Y /100)
#J es el valor del articulo sin IVA
Z = X -J
#Z es el IVA pagado
print(f"El importe sin IVA es :{J:.2f} EUR")
print(f"El IVA pagado es:{Z:.2f} EUR")