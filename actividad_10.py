from unicodedata import category

products = {}

def products_add(num_products):
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

while True:
    print(f"\nINVENTARIO DE TIENDA DE ROPA")
    print(f"1. Añadir producto")
    print(f"2. Inventario completo")
    print(f"3. Buscar producto")
    print(f"4. Precio del inventario")
    print(f"5. Producto por categoria")
    print(f"6. Salir")

    option_user = input(f"Ingrese su opción: ")
    match option_user:
        case "1":
            num_products = int(input(f"\n¿Qué cantidad de productos va a ingresar?: "))
            products_add(num_products)
            print(products)

        case "2":
            print(f"\nInventario completo")
            for code_product, data in products.items():
                print(f"\nCódigo de Producto: {code_product}")
                print(f"Nombre: {data['name']}")
                print(f"Categoria: {data['category']}")
                print(f"Size: {data['size']}")
                print(f"Price: {data['price']}")
                print(f"Stock: {data['stock']}")

        case "3":
            print(f"\nBuscar producto")
            search_product = input(f"Ingrese el código del producto: ").lower()
            if search_product in products:
                product = products[search_product]
                print(f"Producto: {product['name']} ")
                print(f"Categoría: {product['category']}")
                print(f"Tamaño: {product['size']}")
                print(f"Precio: Q{product['price']}")
                print(f"Stock: {product['stock']}")

            else:
                print(f"El producto con ese código no existe")

        case "4":
            print(f"\nPrecio del inventario")
            suma = 0
            for data in products.values():
                suma += data['price'] * data['stock']
            print(f"\nTotal de inventario Q{suma}")

        case "5":
            print(f"\nProducto por categoria")
            category_user = input(f"Ingrese su categoria: ").lower()
            count = 0
            for data in products.values():
                if category_user in data['category']:
                    count += 1
            print(f"\nTotal de productos para {category_user}: {count}")

        case "6":
            print(f"\nSaliendo del inventario")
            break

        case _:
            print(f"\nValor inválido, intentelo de nuevo.")