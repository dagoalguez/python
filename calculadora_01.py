print("--- CALCULADORA MEJORADA ---\nHola, elija una opción:\n")
print("1- Suma.\n2- Resta.\n3- Multiplicación.\n4- División.\n5- Exponente\n")
operador = int(input("Teclee una opción: \n"))

match operador:
    case 1: #suma
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        r = n1 + n2
        print(f"\nLa suma es: {r}")
    case 2: #resta
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        r = n1 - n2
        print(f"\nLa resta es: {r}")
    case 3: #multiplicación
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        r = n1 * n2
        print(f"\nLa multiplicación es: {r}")
    case 4: #division
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        r = n1 / n2
        print(f"\nLa división es: {r}")
    case 5: #eponente
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        r = n1 ** n2
        print(f"\nEl primer número elevado al segundo es: {r}")
    case _:
        print("error")

input("\nPresione Enter para salir...")