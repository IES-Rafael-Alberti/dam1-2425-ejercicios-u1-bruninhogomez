"Este es el ejercicio 28"
#Calcular el área de un triángulo a partir de tres lados


def calcular_semiperimetro(a, b, c):
    s_op = a + b + c / 2
    return s_op

def calcular_area(a, b, c):
    s = calcular_semiperimetro(a, b, c)
    area = s * (s - a) * (s - b) * (s - c)
    return area

def main():
    a = float(input("Introduce el lado a del triángulo: "))
    b = float(input("Introduce el lado b del triángulo: "))
    c = float(input("Introduce el lado c del triángulo: "))
    
    if a + b > c or a + c > b or b + c > a:
        print(f"El área del triángulo es: {calcular_area(a, b, c):.2f}")
    else:
         print("Los lados proporcionados no forman un triángulo válido.")

if __name__ == "__main__":
    main()