from conexion_bd import Conexion

class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuarios WHERE nombre_usuario = %s'
    _INSERTAR = 'INSERT INTO usuarios (nombre, apellido, contrasena, nombre_usuario) VALUES (%s, %s, %s, %s)'
    _CONTRASENA = 'SELECT * FROM usuarios WHERE contrasena = %s'

    @classmethod
    def seleccionar(cls):
        """
        Método para seleccionar un usuario existente.

        El usuario ingresa un nombre de usuario y una contraseña.
        Se realiza una consulta a la base de datos para verificar si el nombre de usuario existe.
        Si existe, se intenta verificar la contraseña ingresada.
        Si la contraseña es correcta, se muestra un mensaje de inicio de sesión exitoso.
        Si la contraseña es incorrecta, se muestra un mensaje de error y se permite hasta 3 intentos.
        Si se alcanza el límite de intentos, se muestra un mensaje de error y se finaliza el proceso.
        Si el nombre de usuario no existe, se muestra un mensaje de error.
        """
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                salida = True
                while salida:
                    nombre_usuario = input("Ingrese un Nombre de Usuario: ")
                    cursor.execute(cls._SELECCIONAR, (nombre_usuario,))
                    registro = cursor.fetchall()
                    if registro:
                        for i in range(1, 4):
                            contrasena = input("Ingrese una Contraseña: ")
                            cursor.execute(cls._CONTRASENA, (contrasena,))
                            registroContra = cursor.fetchall()
                            if registroContra:
                                print(f'Iniciaste sesion como {nombre_usuario}')
                                salida = False
                                break
                            else:
                                print(f'La contrasena es incorrecta, intento {i} de 3')
                                if i == 3:
                                    print('Se alcanzó el límite de intentos, vuelva a intentarlo más tarde')
                    else:
                        print(f'El usuario {nombre_usuario} no existe')

        return nombre_usuario

    @classmethod
    def insertar(cls):
        """
        Método para insertar un nuevo usuario en la base de datos.

        El usuario ingresa su nombre, apellido, nombre de usuario y contraseña.
        Se ejecuta una sentencia INSERT en la base de datos para agregar el nuevo usuario.
        Se retorna el número de filas afectadas por la inserción.
        """
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                nombre = input("Ingrese su Nombre: ")
                apellido = input("Ingrese su Apellido: ")
                nombre_usuario = input("Ingrese un Nombre de Usuario: ")
                contrasena = input("Ingrese una Contraseña: ")
                valores = (nombre, apellido, contrasena, nombre_usuario)
                cursor.execute(cls._INSERTAR, valores)
                return cursor.rowcount

    @classmethod
    def visitante(cls):
        """
        Método para iniciar sesión como visitante.

        Se muestra un mensaje de inicio de sesión como "invitado".
        """
        usuario = "invitado"
        print(f'Iniciaste sesion como {usuario}')

    @staticmethod
    def obtener_usuario_id_actual():
        pass
        """
        Método para obtener el ID del usuario actual.

        Este método debe ser implementado según la lógica de tu aplicación.
        Puedes utilizar variables globales, almacenar el ID en una clase o utilizar otro enfoque según tu implementación.
        Retorna el ID del usuario actual.
        """

# if __name__ == '__main__':
    # INSERTAR USUARIO
    # insertar = UsuarioDAO.insertar()
    # print(insertar)

    # INICIAR SESION
    # seleccionar = UsuarioDAO.seleccionar()
    # print(seleccionar)
