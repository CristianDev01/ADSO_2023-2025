# Algoritmo: Para calcular la nota correspondiente al primer parcial.

taller1 = float(input('Ingrese la calificación del taller 1: '))
taller2 = float(input('Ingrese la calificación del taller 2: '))
quiz = float(input('Ingrese la calificación del quiz: '))
examen_parcial = float(input('Ingrese la calificación del examen parcial: '))

notas_taller_quiz = (taller1 + taller2 + quiz) * 0.3
nota_parcial = examen_parcial * 0.7

nota_final = notas_taller_quiz + nota_parcial

print(f'La nota final del primer parcial de Análisis es: {nota_final:.1f}')