"Este es el ejercicio 5"
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y
# calcule e imprima por pantalla el precio final del artículo.

X = float(input("dame el importe sin IVA del articulo: "))
Y = float(input("introduce el porcentaje del tipo de IVA : "))

articulo = X * (Y/100)

print(f"Valor del articulo con IVA general : {articulo:.2f}")