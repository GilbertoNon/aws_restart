precio = float(input("cual es el precio del producto? "))
if type(precio) != float or precio <= 0:
    print("valor de kmRecorrido invalido!!!!")
    exit()

precioFinal = precio - precio * 0.15
print("el precio final es : ", precioFinal)
