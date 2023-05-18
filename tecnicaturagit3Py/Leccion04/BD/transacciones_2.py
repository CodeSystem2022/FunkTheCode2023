import psycopg2 as bd # esto es para poder conectarnos a postgre

conexion =bd.connect(
    user = 'postgres',
    password='Manaos.22',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    #conexion.autocommit = False esto no deberia estar, inicia la transaccion
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    valores = ("jorge", "prol", "jprol@mail.com")
    cursor.execute(sentencia, valores)

    sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email = %s WHERE id_persona=%s"
    valores = ("juan carlos", "perez", "jcperez@mail.com", 1)
    cursor.execute(sentencia, valores)

    conexion.commit() # hacemos el commit manualmente, se cierra la transaccion
    print("termina la transaccion")
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback {e}')
finally:
    conexion.close()