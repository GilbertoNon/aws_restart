kmRecorrido = float(input("Cuantos km recorrio? "))
if type(kmRecorrido) != float or kmRecorrido <= 0:
    print("valor de kmRecorrido invalido!!!!")
    exit()

    
ltConsumido = float(input("Cuantos litros de gasolina consumio? "))
if type(ltConsumido) != float or ltConsumido <= 0:
    print("valor de ltConsumido invalido!!!!")
    exit()

consumo = kmRecorrido / ltConsumido
print("El consumo es de :", consumo)