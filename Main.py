from inicioSesion import InicioSesion
from Libreria import Libreria
from usuarioDAO import UsuarioDAO
from Carrito import Carrito

def menu_principal():
    usuarios = UsuarioDAO()
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
            # Opción 1: Iniciar sesión
            usuario_id = usuarios.seleccionar()  # Obtener el usuario_id del usuario autenticado

            while True:
                libreria.consultar_libros_por_autor()  # Mostrar lista de libros disponibles
                Carrito.mostrar_libros_comprados(usuario_id)  # Mostrar libros comprados por el usuario

                opcion_continuar = input("¿Desea realizar otra búsqueda? (s/n): ")
                if opcion_continuar.lower() != "s":
                    break
            break

        elif opcion == "2":
            # Opción 2: Crear cuenta
            if usuarios.insertar():
                while True:
                    libreria.consultar_libros_por_autor()  # Mostrar lista de libros disponibles
                    Carrito.mostrar_libros_comprados(None)  # Mostrar libros comprados sin usuario_id

                    opcion_continuar = input("¿Desea realizar otra búsqueda? (s/n): ")
                    if opcion_continuar.lower() != "s":
                        break
                break

        elif opcion == "3":
            # Opción 3: Acceso como visitante
            usuarios.visitante()
            while True:
                libreria.consultar_libros_por_autor()  # Mostrar lista de libros disponibles
                Carrito.mostrar_libros_comprados(None)  # Mostrar libros comprados sin usuario_id

                opcion_continuar = input("¿Desea realizar otra búsqueda? (s/n): ")
                if opcion_continuar.lower() != "s":
                    break
            break

        elif opcion == "4":
            # Opción 4: Salir
            break

        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()
