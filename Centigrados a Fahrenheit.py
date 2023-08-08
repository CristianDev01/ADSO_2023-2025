# Algoritmo de temperatura grados Centigrados a grados Fahrenheit.

while True:
    try:   
        centigrados = float(input("Ingresa la temperatura en Centigrados: "))
        fahrenheit = int((centigrados * 9/5) + 32)

        print(f"{centigrados} °C son {fahrenheit} °F")

        while True:
            continuar = input('¿Desea hacer otra conversión? (si/no) ').lower()
            if continuar == 'si' or continuar == 'sí':
                break
            elif continuar == 'no':
                print('¡Hasta Luego!')
                exit()
            else:
                print("Error: Por favor ingrese 'si' o 'no.'")

    except ValueError:
        print('Error: ¡Ingresa la temperatura en Números!')