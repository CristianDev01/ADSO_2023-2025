# Algoritmo: calcula la hora en el siguiente segundo.

while True:
    try:
        hora = int(input('Ingrese la hora: '))
        minutos = int(input('Ingrese los minutos: '))
        segundos = int(input('Ingrese los segundos: '))
        
        if segundos < 59:
            segundos += 1
        elif minutos < 59:
            minutos += 1
            segundos = 0
        elif hora < 23:
            hora += 1
            minutos = 0
            segundos = 0
        else:
            hora = 0
            minutos = 0
            segundos = 0

        print(f'Hora en el siguiente segundo: {hora:02}:{minutos:02}:{segundos:02}')
        break
        
    except ValueError:
        print('Error: Ingresa formato válido (23:59:59)')