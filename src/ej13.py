"Este es el ejercicio 13"
#Escribir un programa que pida al usuario dos números enteros y muestre 
#por pantalla los siguienteS: "la división de n entre m da un cociente c y
# un resto r", donde n y m son los números introducidos por el usuario, y c 
# y r son el cociente y el resto de la división entera respectivamente.

n = int (input ("introduce el primer numero: "))
m = int (input ("introduce el segundo numero: "))
 
c = n // m 
r = n % m  
print (f"la division entre {n} entre {m} da un cociente de {c} y resto {r}")