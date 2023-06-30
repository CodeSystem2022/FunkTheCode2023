class InicioSesion:
    usuarios_registrados = []

    def __init__(self):
        self.usuario = None
        self.contrasena = None

#Para no crear una cuenta en cada prueba hice un usuario administrador:
    def iniciar_sesion(self):
        self.usuario = input("Ingrese su usuario: ")
        self.contrasena = input("Ingrese su contraseña: ")

        if self.usuario == "admin" and self.contrasena == "admin":
            print("Inicio de sesión exitoso como administrador.")
            return True

        for usuario in self.usuarios_registrados:
            if usuario['nombre_usuario'] == self.usuario and usuario['contraseña'] == self.contrasena:
                print("Inicio de sesión exitoso.")
                return True

        print("Usuario o contraseña incorrectos.")
        return False

    def crear_cuenta(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")

        self.usuarios_registrados.append({
            'nombre': nombre,
            'apellido': apellido,
            'nombre_usuario': nombre_usuario,
            'contraseña': contraseña
        })

        print("Cuenta creada exitosamente.")

#En caso de visitante no pude lograr que NO realice compras, se puede ver
    def acceso_visitante(self):
        self.usuario = "invitado"
        self.contrasena = None
        print("Acceso como visitante.")

