precio_producto = int(input("Ingrese el precio del producto: "))
descuento = 0

if(precio_producto<100):
    descuento = precio_producto * 0.02
else:
    descuento = precio_producto * 0.1

print(f"El monto del descuento es: {descuento}")
print(f"El monto del total es: {precio_producto - descuento}")