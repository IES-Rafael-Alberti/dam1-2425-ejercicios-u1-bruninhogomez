"Este es el ejercicio 5"
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y
# calcule e imprima por pantalla el precio final del artículo.

X = int(input("dame el importe sin IVA del articulo: "))
Y = int("IVA general : ")+str(X * 21%)

articulo = X + Y

print("Valor del articulo con IVA general : "+str(articulo))