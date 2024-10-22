"Este es el ejercicio 16"
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa 
#debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante),
#el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

pan_b_vendido = int(input("Introduce el numero de barras vendidas que no son del día: "))

pan_a = 3.49 

descuento = 0.60 

pan_b = pan_a * (1 - descuento)

coste_final = pan_b * pan_b_vendido

print(f"El precio habitual de una barra de pan es:{pan_a}")
print(f"El descuento que se le hace por no ser presca es:{pan_b}")
print(f"El coste final de todas las barras no fresacas es:{coste_final}")