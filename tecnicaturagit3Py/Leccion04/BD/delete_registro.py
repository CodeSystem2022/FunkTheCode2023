import psycopg2 # esto es para poder conectarnos a postgre

conexion = psycopg2.connect(
    user = 'postgres',
    password='Manaos.22',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = (
                ('juan ','Perez','Jperez@mail.com', 4),
                ("Romina","Ayala","ayalaR@mail.com",5),
            ) # es una tupla de tuplas
            cursor.executemany(sentencia, valores) # de esta manera ejecutamos la sentencia
            registros_actualizados= cursor.rowcount
            print(f"los registros actualizados son:{registros_actualizados}")

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# https_//www.psycopg.org/focs/usage.html
