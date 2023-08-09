# Edades de un grupo de 10 personas en un vector de enteros.

edades = [0] * 10
menores = 0
mayores = 0
adultos_mayores = 0
edad_min = 120 
edad_max = 0
suma_edades = 0

for i in range(10):
  edad = int(input("Ingrese una edad entre 1 y 120: "))
  while edad < 1 or edad > 120:
    print("Edad inválida. Debe estar entre 1 y 120")
    edad = int(input("Ingrese una edad entre 1 y 120: "))
  
  edades[i] = edad
  
  if edad < 18:
    menores += 1
  elif edad >= 18:  
    mayores += 1
  if edad >= 60:
    adultos_mayores += 1
  
  if edad < edad_min:
    edad_min = edad
  if edad > edad_max:
    edad_max = edad
      
  suma_edades += edad

promedio = suma_edades / 10

print("Menores:", menores)
print("Mayores:", mayores)
print("Adultos mayores:", adultos_mayores) 
print("Edad mínima:", edad_min)
print("Edad máxima:", edad_max)
print("Promedio de edad:", round(promedio))