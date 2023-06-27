import psycopg2 # conectamos postgre

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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input("digite un numero para el id_persona: ")
            cursor.execute(sentencia,(id_persona,)) # ejecutamos sentencia
            registros = cursor.fetchone() # recuperamos todos los registros que seran una lista
            print(registros)


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
