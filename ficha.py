def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    nombre_apellido = input("Ingrese nombre: ").title().strip()
    email = input("Ingrese su email: ").lower()
    nota_1 = int(input("Ingrese nota 1: "))
    nota_2 = int(input("Ingrese nota 2: "))
    nota_3 = int(input("Ingrese nota 3: "))
    espacio = nombre_apellido.find(" ")
    nombre = nombre_apellido[:espacio]
    apellido = nombre_apellido[espacio+1:]
    arroba = email.find("@")
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    print(f"""========================
    FICHA DEL ALUMNO
========================""")

    #   - Nombre limpio: sin espacios extra y con formato título
    print(f"Nombre: {nombre_apellido.title().strip()}")

    #   - Email en minúsculas
    print(f"Email: {email.lower()}")

    #   - Cantidad de caracteres del nombre
    print(f"Caracteres en nombre: {len(nombre_apellido)}")

    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    print(f"Iniciales: {nombre[0].capitalize()}{apellido[0].capitalize()}")
    #   - Usuario: apellido.nombre en minúsculas
    print(f"Usuario: {apellido.lower()}.{nombre.lower()}")
    #   - Verificar si el email contiene @
    print(f"Email valido: {'@' in email}")
    #   - Extraer el dominio del email
    print(f"Dominio: {email[arroba+1:]}")
    #   - Nombre con guion bajo en vez de espacio
    print(f"Nombre para archivo: {nombre_apellido.replace(' ', '_')}")
    #   - Contar las 'a' en el nombre

    print(f"Cantidad de a: {nombre_apellido.count('a')}")
    #   - Código secreto: nombre invertido en mayúsculas
    print(f"Codigo secreto: {nombre_apellido[::-1].upper()}")
    #   - Las 3 notas, su suma, promedio y promedio entero
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    suma = nota_1 + nota_2 + nota_3
    print(f"Suma: {int(suma)}")
    print(f"Promedio: {(float(suma)/3)}")
    print(f"Promedio entero: {int((float(suma)/3))}")

    #   - Cierre decorativo usando repetición de string ("=" * 24)
    print("=" * 24)
    pass