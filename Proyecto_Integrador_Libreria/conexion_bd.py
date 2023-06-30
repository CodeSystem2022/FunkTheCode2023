import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'test_baseDatos'  # Nombre de la base de datos
    _USERNAME = 'postgres'  # Nombre de usuario para acceder a la base de datos
    _PASSWORD = '5648'  # Contraseña del usuario para acceder a la base de datos
    _DB_PORT = '5432'  # Puerto de la base de datos
    _HOST = '127.0.0.1'  # Dirección IP del host de la base de datos
    _conexion = None  # Variable para almacenar la conexión a la base de datos
    _cursor = None  # Variable para almacenar el cursor de la base de datos

    @classmethod
    def obtenerConexion(cls):
        """
        Método estático que obtiene una conexión a la base de datos.

        Si la variable de clase _conexion es None, indica que no hay una conexión abierta,
        por lo que se crea una nueva conexión utilizando los valores de configuración predefinidos.
        Si se produce algún error durante la conexión, se muestra un mensaje de error y se termina el programa.
        Si ya hay una conexión abierta, se devuelve esa conexión.

        Returns:
            psycopg2.extensions.connection: Objeto de conexión a la base de datos.
        """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                print(f'Conexion Exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Método estático que obtiene un cursor para ejecutar consultas en la base de datos.

        Si la variable de clase _cursor es None, indica que no hay un cursor abierto,
        por lo que se crea un nuevo cursor utilizando la función obtenerConexion().
        Si se produce algún error durante la creación del cursor, se muestra un mensaje de error y se termina el programa.
        Si ya hay un cursor abierto, se devuelve ese cursor.

        Returns:
            psycopg2.extensions.cursor: Objeto de cursor para ejecutar consultas en la base de datos.
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._cursor
