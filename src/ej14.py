"Este es el ejercicio 14"
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de 
#cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
#en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
#pedido y calcule el peso total del paquete que será enviado.

payasos =  112  
muñecas = 75 
num_payasos = int(input("Introduce el numero de payasos vendidos: "))
num_muñecas = int(input("Introduce el numero de muñecas vendidas: "))
peso = (payasos*num_payasos)+(muñecas*num_muñecas)
print(f"El peso total del pedido sería : {peso}gramos")