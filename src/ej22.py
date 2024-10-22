"Este es el ejercicio 22"
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.




def pedir_entrada(msj: str):
    entrada = input(msj)
    return entrada


def comprobar_vocal(vocal: str) -> bool:
    if len(vocal) == 1 and vocal in "aeiou":
        return True
    else:
        return False


def cambiar_frase(frase: str, vocal: str):
    return frase.replace(vocal,vocal.upper())
    

def main():
    frase = pedir_entrada("Introduce una frase a la consola: ")
    vocal = pedir_entrada("Introduce una vocal: ").lower()
    if comprobar_vocal(vocal) == True:
        print(f"La frase será: {cambiar_frase(frase, vocal)}")
    else:
        print("ERROR")

if __name__ == "__main__":
    main()