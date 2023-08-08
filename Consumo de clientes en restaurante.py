# Algoritmo: consumo de clientes en restaurante con descuesto en compras +50000

num_clientes = int(input("Ingrese el número de clientes: "))

total_pagos = 0

for i in range(1, num_clientes + 1):
    consumo = float(input(f"Ingrese el consumo del cliente {i} en pesos: "))
    
    if consumo > 50000:
        descuento = 0.2 * consumo
        pago = consumo - descuento
    else:
        descuento = 0
        pago = consumo
    
    total_pagos += pago
    
    print(f"Cliente {i}:")
    print(f"Consumo: {int(consumo)} pesos")
    print(f"Descuento: {int(descuento)} pesos")
    print(f"Pago: {int(pago)} pesos\n")
    
print(f"Total de todos los pagos: {int(total_pagos)} pesos")
