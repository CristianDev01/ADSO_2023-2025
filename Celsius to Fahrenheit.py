# Algoritmo de temperatura Celcius a Fahrenheit.

while True:
    try:   
        celsius = float(input("Ingresa la temperatura de NY en Celsius: "))
        fahrenheit = round(celsius * 1.8 + 32)

        print(f"{celsius} °C son {fahrenheit} °F En Nueva York")

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