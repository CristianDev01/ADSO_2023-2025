# Algoritmo: Escribir el producto desde 1 hasta N.

def producto(n):
  resultado = 1
  for i in range(1, n+1):
    resultado *= i
  return resultado

n = int(input("Ingresa un número: "))
print(producto(n))