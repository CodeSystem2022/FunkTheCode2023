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
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)' #placeholder
            valores = (
                ("calos", "lara", "clara@mail.com"),
                ("Marcos","Canto","mcanto@mail.com"),
                ("Marcelo","Cuenca","ccanta@gmail.com")
            )# es una tupla de tuplas
            cursor.executemany(sentencia, valores) # de esta manera ejecutamos la sentencia
            # conexion.commit() esto se utilia para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f"los registros insertados son:{registros_insertados}")

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# https_//www.psycopg.org/focs/usage.html
# https_//www.psycopg.org/focs/usage.html