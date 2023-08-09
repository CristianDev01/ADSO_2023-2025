# Área y perímetro de figuras planas.

# Primera Figura: Triángulo.
lado1 = 10 
lado2 = 10
base = 6
altura = 8

perimetro = lado1 + lado2 + base
print("Perímetro del triángulo:", perimetro)

area = (base * altura) / 2
print("Área del triángulo:", area)

# Segunda Figura: Rectangulo.
base = 12 
altura = 5

perimetro = 2 * (base + altura)
print("Perímetro del rectangulo:", perimetro)

area = base * altura
print("Área del rectangulo:", area)

# Tercera Figura: Cuadrado.
a = 5

perimetro = 4 * a
print("Perímetro del cuadrado:", perimetro)

area = a ** 2  
print("Área del cuadrado:", area)

# Cuarta Figura: Círculo
import math

r = 5

perimetro = 2 * math.pi * r 

area = math.pi * r**2

print("Perímetro del círculo:", round(perimetro, 2)) 
print("Área del círculo:", round(area, 2))