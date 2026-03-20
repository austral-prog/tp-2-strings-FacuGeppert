def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {base * altura}")
    print(f"Perimetro: {(base*2) + (altura*2)}")
    pass
