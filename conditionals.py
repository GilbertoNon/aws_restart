"""
Your module description
"""
userReply = input("necesitas entregar un paquete?").capitalize()

if userReply == "Si":
    print("podemos ayudante con la entrega")
else:
    print("vuelve cuando lo necesites")
    exit()
    
userReply = input("que te gustaria compar: estampas, sobre, copia").lower()

if userReply == "estampas":
    print("tenemos muchos diseños")
elif userReply == "sobre":
    print("tenemos muchos sobres")
elif userReply == "copia":
    copies = input("Cuantas  copias quiere? ")
    print("Se sacara ", copies)
else:
    print("gracias")