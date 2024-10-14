"Este es el ejercicio 6"
#Escribe un programa que pida el importe final de un artículo 
#y calcule e imprima por pantalla el IVA que se ha pagado y el importe 
#sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

x = float(input("introduzca el importe con IVA : "))
#x es el valor del artículo
y = 10
#y es tipo de IVA 
j = x / (1 + y /100)
#j es el valor del articulo sin IVA
z = x -j
#z es el IVA pagado
print(f"El importe sin IVA es :{j:.2f} EUR")
print(f"El IVA pagado es:{z:.2f} EUR")