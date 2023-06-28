#Código Bárbara
'''
from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log


class PersonaDAO:
    """
    dao significa :data access object
    crud significa:
    create -> insertar
    read -> seleccionar
    Update -> actualizar
    delete ->Eliminar
    """

    _SELECCIONAR = 'SELECT *FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET  nombre=%s , apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # definimos los metodos de la clase:

    @classmethod
    def seleccionar(cls):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []  # creamos una lista
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
    @classmethod
    def insert(cls, persona):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                valores=(persona.nombre,persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada:{persona}.')
                return cursor.rowcount

    @classmethod
    def actualizar (cls,persona):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                valores = (persona.nombre,persona.apellido, persona.email, persona._id_persona)
                cursor.execute (cls._ACTUALIZAR,valores)
                log.debug(f'persona actualizada:{persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                valores = (persona._id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'persona eliminada:{persona}')
                return cursor.rowcount



if __name__ == '__main__':
    #eliminar un registro:
    #persona1 =Persona(id_persona=58)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'personas eliminadas:{personas_eliminadas}')


    #Actualizar un registro:
    #persona1 = Persona(62,'Guido', 'Peña', 'GPeña@gmail.com' )
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas:{personas_actualizadas}')

    #insertar un registro
    #persona1= Persona(nombre='Elian', apellido='Jimenez', email='ElianJimenez@hotmail.com')
    #personas_insertadas = PersonaDAO.insert(persona1)
    #log.debug(f'personas insertadas.{personas_insertadas}')
    #seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
'''
#Código Catriel
from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log


class PersonaDAO:
    """
    dao significa :data access object
    crud significa:
    create -> insertar
    read -> seleccionar
    Update -> actualizar
    delete ->Eliminar
    """

    _SELECCIONAR = 'SELECT *FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET  nombre=%s , apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # definimos los metodos de la clase:

    @classmethod
    def seleccionar(cls):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []  # creamos una lista
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
    @classmethod
    def insert(cls, persona):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                valores=(persona.nombre,persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada:{persona}.')
                return cursor.rowcount

    @classmethod
    def actualizar (cls,persona):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                valores = (persona.nombre,persona.apellido, persona.email, persona._id_persona)
                cursor.execute (cls._ACTUALIZAR,valores)
                log.debug(f'persona actualizada:{persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.cbtenerConexion():
            with Conexion.obtenercursor() as cursor:
                valores = (persona._id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'persona eliminada:{persona}')
                return cursor.rowcount



if __name__ == '__main__':
    #eliminar un registro:
    #persona1 =Persona(id_persona=58)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'personas eliminadas:{personas_eliminadas}')


    #Actualizar un registro:
    #persona1 = Persona(62,'Guido', 'Peña', 'GPeña@gmail.com' )
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas:{personas_actualizadas}')

    #insertar un registro
    #persona1= Persona(nombre='Elian', apellido='Jimenez', email='ElianJimenez@hotmail.com')
    #personas_insertadas = PersonaDAO.insert(persona1)
    #log.debug(f'personas insertadas.{personas_insertadas}')
    #seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

