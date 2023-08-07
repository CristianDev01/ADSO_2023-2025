# Algoritmo Conversión dolares a pesos colombianos.

while True:
    try:
        usd = float(input('Ingrese la cantidad en USD: ')) 
        tasa_de_cambio = 4100
        conversion_cop = int(usd * tasa_de_cambio)

        print(f'{usd} Dolares equivalen a {conversion_cop} Pesos Colombianos')
        
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
        print('Error: ¡Escribe solo números!')