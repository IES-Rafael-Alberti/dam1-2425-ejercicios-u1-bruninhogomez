"Este es el ejercicio 21"
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

def pedir_frase():
    frase = input("Introduce una frase: ")
    return frase
 

def main():
    invertida = pedir_frase()
    print(f"La frase invertida será: {invertida[::-1]}")

if __name__ == "__main__":
    main()