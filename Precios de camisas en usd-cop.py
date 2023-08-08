# 5 precios de camisas (en dólares) y que luego muestre el total la venta en pesos.

precios_camisas = []

for i in range(5):
    while True:
        try:
            precio = float(input(f"Precio de la camisa {i + 1} en USD: "))
            precios_camisas.append(precio)
            break
        except ValueError:
            print("Error: Ingrese un número válido.")

total_dolares = 0

for precio in precios_camisas:
    total_dolares += precio

tasa_conversion_usd = 4100
total_pesos = total_dolares * tasa_conversion_usd

print(f'Total de la venta en dolares: {int(total_dolares)} USD')
print(f'Total de la venta en pesos: {int(total_pesos)} COP')