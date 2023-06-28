from inicioSesion import InicioSesion
from Libreria import Libreria

'''
 usuario: admin
 clave: admin
 
 -El codigo envia directamente a una busqueda por autor una vez nos logeamos.
 -Se pueden agregar busquedas por otras referencias, habria que ver la API de google books: https://developers.google.com/books/docs/overview?hl=es-419
 -Arroja 5 libros del autor y se debe seleccionar cual comprar
 -Una vez hecha la compra reedirecciona a una busqueda en mercadolibre (Esto fue para evitar el tema de mostrar el precio, ya que la api no es constante con los precios.
 -Una vez hecha la compra muestra los datos del libro y consulta si queremos seguir comprando
 '''

def menu_principal():
    inicio_sesion = InicioSesion()
    libreria = Libreria()
    while True:
        print("Bienvenido a la Librería Virtual")
        print("-----------------------------")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Acceso como visitante")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            if inicio_sesion.iniciar_sesion():
                while True:
                    libreria.consultar_libros_por_autor()
                    opcion_continuar = input("¿Desea realizar otra búsqueda? (s/n): ")
                    if opcion_continuar.lower() != "s":
                        break
                break
        elif opcion == "2":
            inicio_sesion.crear_cuenta()
        elif opcion == "3":
            inicio_sesion.acceso_visitante()
            while True:
                libreria.consultar_libros_por_autor()
                opcion_continuar = input("¿Desea realizar otra búsqueda? (s/n): ")
                if opcion_continuar.lower() != "s":
                    break
            break
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu_principal()
