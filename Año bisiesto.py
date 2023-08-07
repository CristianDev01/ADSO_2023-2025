# Algoritmo: Determinar si un año indicado es o no un año bisiesto.

def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input('Ingresa el año: '))

if año_bisiesto(año):
    print(año,'Es un año bisiesto')
else:
    print(año,'No es un año bisiesto')