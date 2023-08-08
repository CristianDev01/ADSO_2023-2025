# Algoritmo de temperatura grados Fahrenheit a grados Centigrados.

while True:
    try:   
        fahrenheit = float(input("Ingresa la temperatura de NY en Fahrenheit: "))
        centigrados = int((fahrenheit - 32) * 5/9)

        print(f"{fahrenheit} °F son {centigrados} °C En Nueva York")

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