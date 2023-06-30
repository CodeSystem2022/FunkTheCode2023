from conexion_bd import Conexion
from LibroDAO import LibroDAO
from usuarioDAO import UsuarioDAO

class Carrito:
    libros_comprados = []

    @staticmethod
    def agregar_libro(producto):
        libro = {
            "titulo": producto.titulo,
            "autor": producto.autor,
            "precio": producto.precio,
        }
        Carrito.libros_comprados.append(libro)

    @staticmethod
    def mostrar_libros_comprados(usuario_id=None):

        usuario_id = UsuarioDAO.obtener_usuario_id_actual()  # Obtener el ID del usuario actual
        print("Libros comprados:")
        if len(Carrito.libros_comprados) > 0:
            for i, libro in enumerate(Carrito.libros_comprados, 1):
                print(f"{i}. Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Precio: ${libro['precio']}")
                print("--------------------")

            # Guardar los libros comprados en la base de datos
            LibroDAO.guardar_libros_comprados(Carrito.libros_comprados, usuario_id)

        else:
            print("No se han comprado libros aún.")
