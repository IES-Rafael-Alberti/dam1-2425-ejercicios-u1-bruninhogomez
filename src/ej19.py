"Este  es el ejercicio 19"
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
#introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas 
#y n es el número de letras que tienen el nombre.
def main():

    nombre = input("Introduce tu nombre completo: ")
    n_letras = len(nombre)
    print(f"{nombre.upper} tiene {n_letras} letras.")

if __name__=="__main__":
    main()