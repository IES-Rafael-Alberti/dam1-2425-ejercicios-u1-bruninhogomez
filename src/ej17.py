"""
Ej 17

Este algoritmo imprime por pantalla el nombre del usuario las veces que el lo pida


"""

"Este es el ejercicio 17"
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
#por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Introduzca su nombre : ")

numero = int(input("Introduce un numero entero : "))

for _ in range(numero) :
    print(nombre)