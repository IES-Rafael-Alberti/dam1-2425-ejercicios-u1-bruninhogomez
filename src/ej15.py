"Este es el ejercicio 15"
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
#Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
#Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
#Redondear cada cantidad a dos decimales.

cantidad = float (input("Introduce la cantidad de dinero depositada en la cuenta: "))
interés = 0.04 

saldo_1 = cantidad * (1+interés)
saldo_2 = saldo_1 * (1+interés)
saldo_3 = saldo_2 * (1+interés)

print(f"saldo tras el primer año: {saldo_1:.2f}")
print(f"saldo tras el segundo año: {saldo_2:.2f}")
print(f"saldo tras el tercer año : {saldo_3:.2f}")