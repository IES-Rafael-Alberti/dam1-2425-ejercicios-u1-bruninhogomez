"Este es el ejercicio 20"
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el
#código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa 
#que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el 
#prefijo y la extensión.
def pedir_num():
    num = input("Introduce el numero de telefono: ")
    return num

def separar_num(num):
    num.split("-")

def main():
    num = pedir_num()
    num = separar_num(num)

if __name__ == "__main__":
    main()