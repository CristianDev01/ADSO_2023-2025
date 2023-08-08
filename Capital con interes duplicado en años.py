# Algoritmo: Capital con tasa de interes que se duplica en (X) años.

capital_inicial = float(input('Ingrese el capital inicial: '))
interes_anual = float(input('Ingrese el interes anual: '))

interes_tea = interes_anual / 100
capital_final = capital_inicial * 2

tiempo_en_años = 0
while capital_inicial < capital_final:
    capital_inicial *= (1 + interes_tea)
    tiempo_en_años += 1
    
print(f'El capital se doblará después de {tiempo_en_años} años')