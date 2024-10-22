"Este es el ejercicio 25"
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y
#muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
#funcione cuando el día o el mes se introduzcan con un solo carácter.

nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, año = nacimiento.split("/")

dia = dia.zfill(2)
mes = mes.zfill(2)

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")