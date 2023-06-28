import webbrowser

class Producto:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_informacion(self):
        print("Información del libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.precio}")

#Busqueda en Mercadolibre
    def comprar(self):
        opcion = input("¿Desea comprar este libro? (s/n): ")
        if opcion.lower() == "s":
            # Realizar la búsqueda en MercadoLibre
            busqueda = f"{self.titulo} {self.autor} libro"
            url_mercadolibre = f"https://www.mercadolibre.com.ar/jm/search?as_word={busqueda}"
            webbrowser.open(url_mercadolibre)
            print("¡Compra realizada con éxito!")
        else:
            print("Compra cancelada.")

