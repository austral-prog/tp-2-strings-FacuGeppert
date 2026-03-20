def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto=float(input("Ingresar costo:"))
    dinero=int(input("Dinero recibido"))
    
    vuelto = int(dinero - gasto)
    centavos = round((((dinero - gasto)) - vuelto)*100)
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(vuelto)
    print("Centavos:")
    print(centavos)
