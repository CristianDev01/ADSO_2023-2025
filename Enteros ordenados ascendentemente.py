# Dos vectores de números enteros ordenados ascendentemente y mezclados.

def leer_vector(mensaje):
    vector = []
    print(mensaje)
    for i in range(5):
        while True:
            try:
                num = int(input(f"Ingrese el número {i+1} del vector: "))
                if i > 0 and num <= vector[i-1]:
                    print("El número debe ser mayor que el número anterior.")
                else:
                    vector.append(num)
                    break
            except ValueError:
                print("Debe ingresar un número entero.")
    return vector

vector1 = leer_vector("Ingrese los elementos del primer vector:")
vector2 = leer_vector("\nIngrese los elementos del segundo vector:")

mezcla = []
i = j = 0

while i < len(vector1) and j < len(vector2):
    if vector1[i] < vector2[j]:
        mezcla.append(vector1[i])
        i += 1
    else:
        mezcla.append(vector2[j])
        j += 1

mezcla.extend(vector1[i:])
mezcla.extend(vector2[j:])

print("\nLa lista ordenada de la mezcla de los dos vectores es:")
print(mezcla)