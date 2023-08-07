# Algoritmo: Determinar edad actual apartir de fecha de nacimiento en año actual.

while True:
    try:
        fecha_nacimiento = input('Ingresa tu fecha de nacimiento (DD/MM/AAAA): ')
        dia_nacimiento, mes_nacimiento, año_nacimiento = fecha_nacimiento.split('/')
        año_nacimiento = int(año_nacimiento)

        from datetime import datetime
        año_actual = datetime.now().year
        edad = año_actual - año_nacimiento 

        print("Tu edad actual es:", edad, 'Años')
        break

    except ValueError:
        print('Error: Formato invalido! ')
        continue