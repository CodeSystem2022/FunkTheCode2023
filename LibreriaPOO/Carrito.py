class Carrito:
    libros_comprados = []

    @staticmethod
    def agregar_libro(producto):
        Carrito.libros_comprados.append({
            "titulo": producto.titulo,
            "autor": producto.autor,
            "precio": producto.precio
        })

    @staticmethod
    def mostrar_libros_comprados():
        print("Libros comprados:")
        if len(Carrito.libros_comprados) > 0:
            for i, libro in enumerate(Carrito.libros_comprados, 1):
                print(f"{i}. Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Precio: ${libro['precio']}")
                print("--------------------")
        else:
            print("No se han comprado libros aún.")

#aca se almacenan datos de los libros