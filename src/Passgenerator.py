import random
import string


# -------------------------------
# Validar la longitud ingresada
# -------------------------------
def obtener_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud >= 4:
                return longitud
            else:
                print("La longitud debe ser mayor o igual a 4.\n")
        except ValueError:
            print("Debe ingresar un número.\n")

4
# -------------------------------
# Seleccionar los caracteres
# -------------------------------
def obtener_caracteres():

    caracteres = ""

    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower()
    minusculas = input("¿Incluir minúsculas? (s/n): ").lower()
    numeros = input("¿Incluir números? (s/n): ").lower()
    simbolos = input("¿Incluir símbolos? (s/n): ").lower()

    if mayusculas == "s":
        caracteres += string.ascii_uppercase

    if minusculas == "s":
        caracteres += string.ascii_lowercase

    if numeros == "s":
        caracteres += string.digits

    if simbolos == "s":
        caracteres += "#_-@"

    return caracteres


# -------------------------------
# Generar contraseña
# -------------------------------
def generar_password(longitud, caracteres):
    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    return password


# -------------------------------
# Programa principal
# -------------------------------
def main():

    print("===================================")
    print(" GENERADOR SEGURO DE CONTRASEÑAS")
    print("===================================\n")

    while True:

        longitud = obtener_longitud()

        caracteres = obtener_caracteres()

        if caracteres == "":
            print("\nDebe seleccionar al menos un tipo de carácter.\n")
            continue

        password = generar_password(longitud, caracteres)

        print("\nContraseña generada:")
        print(password)

        opcion = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

        if opcion != "s":
            break

    print("\nGracias por utilizar el programa.")


main()