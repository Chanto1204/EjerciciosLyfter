print("---Precio del producto---")

product_price = float(input("Ingrese el precio del producto: "))

if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

final_price = product_price - discount

print(f"Tu descuento sera de: {discount}")
print(f"El precio final con el descuento es de: {final_price}")
