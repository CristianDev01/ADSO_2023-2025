# Algoritmo: permite ingresar 20 números y muestra todos los números menores e iguales a 25. 

def obtener_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Error: Ingrese un número válido')

numeros = []

for i in range (20):
    mensaje = (f'Ingrese el número {i + 1}:' )
    numero = obtener_numero(mensaje)
    numeros.append(numero)

print('Números iguales a 25:')
for numero in numeros:
    if numero <= 25:
        print(numero)