def casting():
    """Lee precio, descuento y cantidad como texto y calcula 
    el precio con descuento y el total."""
    precio = int(input("Ingrese el precio:"))
    descuento = float(input("Ingrese el porcentaje del descuento:"))
    cantidad = int(input("Ingrese la cantidad que desea comprar:"))

    precio_final = precio - descuento
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_final}")
    print(f"Total: {precio_final * cantidad}")
    pass