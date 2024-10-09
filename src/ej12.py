"Este es el ejercicio 12"
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
#pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal 
# calculado redondeado con dos decimales.


peso = float(input("Introduce el peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = peso /(estatura ** 2)

print(f"Tu indice de masa corporal es: {imc:.2f}")