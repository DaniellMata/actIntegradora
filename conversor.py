
TASA_MXN_USD = 17.5  # 1 USD = 17.5 MXN (tasa fija definida en el programa)


def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def km_a_millas(km):
    return km * 0.621371


def millas_a_km(millas):
    return millas / 0.621371


def pesos_a_dolares(pesos, tasa=TASA_MXN_USD):
    return pesos / tasa


def dolares_a_pesos(dolares, tasa=TASA_MXN_USD):
    return dolares * tasa


def validar_numero(texto):
    """Convierte texto a float. Lanza ValueError si no es un numero valido (RNF02)."""
    return float(texto)


OPCIONES = {
    "1": ("Celsius a Fahrenheit", celsius_a_fahrenheit),
    "2": ("Fahrenheit a Celsius", fahrenheit_a_celsius),
    "3": ("Kilometros a Millas", km_a_millas),
    "4": ("Millas a Kilometros", millas_a_km),
    "5": ("Pesos (MXN) a Dolares (USD)", pesos_a_dolares),
    "6": ("Dolares (USD) a Pesos (MXN)", dolares_a_pesos),
}


def menu():
    print("\n=== Conversor de unidades ===")
    for clave, (nombre, _) in OPCIONES.items():
        print(f"{clave}. {nombre}")
    print("0. Salir")


def main():
    while True:
        menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "0":
            print("Hasta luego.")
            break

        if opcion not in OPCIONES:
            print("Opcion no valida, intenta de nuevo.")
            continue

        nombre, funcion = OPCIONES[opcion]
        valor_texto = input(f"Ingresa el valor a convertir ({nombre}): ").strip()

        try:
            valor = validar_numero(valor_texto)
        except ValueError:
            print("Error: debes ingresar un valor numerico.")
            continue

        resultado = funcion(valor)
        print(f"Resultado: {resultado:.2f}")  # RNF01: al menos 2 decimales


if __name__ == "__main__":
    main()
