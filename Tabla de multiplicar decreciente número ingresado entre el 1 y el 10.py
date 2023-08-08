# Algoritmo: Tabla de multiplicar decreciente de cualquier número, ingresado entre el 1 y el 10.

numero = int(input("Ingresa un número entre 1 y 10: "))

while numero < 1 or numero > 10:
    print("Número no válido. Debe estar entre 1 y 10")
    numero = int(input("Ingresa otro número: "))

print(f"Tabla del {numero}:")

for i in range(10, 0, -1):
    print(f"{numero} x {i} = {numero*i}")