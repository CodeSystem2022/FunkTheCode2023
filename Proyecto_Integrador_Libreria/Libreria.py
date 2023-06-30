import requests
import webbrowser
from Producto import Producto 
from Carrito import Carrito
from usuarioDAO import UsuarioDAO


class Libreria:
    def __init__(self):
        self.autor = None
        self.titulo = None
        self.codigo = None

    def consultar_libros_por_autor(self):
        self.autor = input("Ingrese el autor del libro que busca: ")
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"inauthor:{self.autor}",
            "maxResults": 5
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "items" in data:
            libros = data["items"]
            for i, libro in enumerate(libros, 1):
                titulo = libro["volumeInfo"].get("title", "Sin título")
                autor = libro["volumeInfo"].get(
                    "authors", ["Autor desconocido"])[0]
                precio = libro["saleInfo"].get("listPrice", {}).get(
                    "amount", "Precio desconocido")
                print(f"{i}. Título: {titulo}")
                print(f"Autor: {autor}")
                print(f"Precio: ${precio}")
                print("--------------------")

            opcion = int(
                input("Seleccione el número de libro que desea comprar: "))
            if opcion > 0 and opcion <= len(libros):
                libro_seleccionado = libros[opcion - 1]
                titulo = libro_seleccionado["volumeInfo"].get(
                    "title", "Sin título")
                autor = libro_seleccionado["volumeInfo"].get(
                    "authors", ["Autor desconocido"])[0]
                precio = libro_seleccionado["saleInfo"].get(
                    "listPrice", {}).get("amount", "Precio desconocido")
                producto = Producto(titulo, autor, precio)
                producto.mostrar_informacion()
                producto.comprar()

                # Autenticacion de usuarios
                usuario_id = UsuarioDAO.seleccionar()
                Carrito.agregar_libro(producto)
                Carrito.mostrar_libros_comprados(usuario_id)
            else:
                print("Opción inválida. Intente nuevamente.")
        else:
            print("No se encontraron libros del autor especificado.")

    def seleccionar_libro(self):

        opcion = input("Seleccione el número de libro que desea comprar: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 5:
                return opcion - 1
        print("Opción inválida. Intente nuevamente.")
        return None
