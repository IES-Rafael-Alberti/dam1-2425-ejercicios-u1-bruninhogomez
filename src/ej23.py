"Este es el ejercicio 23"
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
#pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Introduce tu correo electronico: ")

correo_2 = correo.split("@")[0]

correo_3 = correo_2 + "@ceu.es"

print("Tu nuevo correo electronico es:",correo_3)