products = {}
num_products = int(input(f"\n¿Qué cantidad de productos va a ingresar?: "))
for i in range(num_products):
    print(f"\nProducto: {i + 1}")

    while True:
        code_product = input("Ingrese el código del producto: ").lower()
        if code_product not in products:
            break
        else:
            print(f"El código '{code_product}' ya está registrado. Intente con otro.")

    name_product = input(f"Ingrese el nombre del producto (playera, pantalón, etc.): ")
    category_product = input(f"Ingrese la categoría del producto (hombre, mujer, niño): ").lower()
    size_product = input(f"Ingrese el tamaño del producto (xs, s, m, l, xl, xxl): ")
    while True:
        price_product = int(input(f"Ingrese el precio unitario del producto: Q"))
        if price_product > 0:
            break
        else:
            print(f"El producto debe de ser mayor a Q0")
    while True:
        stock_product = int(input(f"Ingrese el stock del producto: "))
        if stock_product > 0:
            break
        else:
            print(f"El producto debe ser positivo")

    products[code_product] = {
        "name": name_product,
        "category": category_product,
        "size": size_product,
        "price": price_product,
        "stock": stock_product
    }
print(f"\nLISTA DE PRODUCTOS")
for code_product, data in products.items():
    print(f"\n{data["name"].upper()} - {code_product.upper()}")
    print(f"Categoría: {data['category']}")
    print(f"Tamaño: {data['size']}")
    print(f"Precio: Q{data['price']}")
    print(f"Stock: {data['stock']}")

while True:
    search_product = input(f"\nIngrese el código del producto: ").lower()
    if search_product in products:
        product = products[search_product]
        print(f"Producto: {product['name'].upper()}")
        print(f"Categoria: {product['category']}")
        print(f"Tamaño: {product['size']}")
        print(f"Precio: Q{product['price']}")
        print(f"Stock: {product['stock']}")
        break

    else:
        print(f"\nEl producto con ese código no existe, intentelo de nuevo.")

suma = 0
for data in products.values():
    suma += data['price'] * data['stock']
print(f"\n***********************************")
print(f"Precio del inventario: Q{suma}")
print(f"***********************************")
