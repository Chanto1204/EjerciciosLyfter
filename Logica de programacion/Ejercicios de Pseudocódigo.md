1. Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
* Si el precio es menor a 100, el descuento es del 2%.
* Si el precio es mayor o igual a 100, el descuento es del 10%.

Ejemplos:

&#x09;120 → 108

&#x09;40 → 39.2



1. Inicio
2. Definir \[Precio\_Producto]= 0
3. Definir \[Descuento]
4. Definir \[Precio\_Final]
5. Mostrar "Ingrese el precio del producto"
6. Pedir \[Precio\_Producto]
7. Si (\[Precio\_Producto] < 100) entonces:

   1. \[Descuento] = (\[Precio\_Producto] \* 0.02) 
8. Sino:

   1. \[Descuento] = (\[Precio\_Producto] \* 0.10)
9. Finsi
10. \[Precio\_Final] = \[Precio\_Producto] - \[Descuento]
11. Mostrar "El precio final es: "
12. Mostrar \[Precio\_Final]
13. Fin









2- Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

Ejemplos:

1040 → Mayor

140 → 460

600 → Igual

599 → 1



1. Inicio
2. Definir \[Tiempo\_Segundos]
3. Definir \[Faltante]
4. Mostrar "Ingrese un tiempo en segundos:"
5. Pedir \[Tiempo\_Segundos]
6. Si (\[Tiempo\_Segundos] < 600) entonces:

   1. \[Faltante] = 600 - \[Tiempo\_Segundos]
   2. Mostrar = \[Faltante]
7. Sino:

   1. Si (\[Tiempo\_Segundos] = 600) entonce: 

      1. Mostrar "Igual" 
   2. Sino:

      1. Mostrar "Mayor"
   3. FinSi
8. FinSi
9. Fin









3- Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.

5 → 15 (1 + 2 + 3 + 4 + 5)

3 → 6 (1 + 2 + 3)

12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)





1. Inicio
2. Definir \[Numero]
3. Definir \[Suma] = 0
4. Definir \[i]
5. Mostrar "Ingrese un número"
6. Pedir \[Numero]
7. Para \[i] = 1 hasta \[Numero] hacer: 

   1. \[Suma] = \[Suma] + \[i]
8. FinPara
9. Mostrar "La suma es"
10. Mostrar \[Suma]
11. Fin











