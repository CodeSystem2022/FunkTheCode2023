from conexion_bd import Conexion

class LibroDAO:
    _INSERTAR = 'INSERT INTO libros_compra (autor, titulo, usuario_id) VALUES (%s, %s, %s)'

    @classmethod
    def guardar_libros_comprados(cls, libros, usuario_id):

        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                for libro in libros:
                    valores = (
                        libro['autor'],
                        libro['titulo'],
                        usuario_id
                    )
                    cursor.execute(cls._INSERTAR, valores)

                conexion.commit()  # Guardar los cambios en la base de datos

            print("Los libros comprados han sido guardados en la base de datos.")
