'''from NumerosIgualesExcepciones import NumerosIgualesExcepciones

resultado = None

try:
    a = int(input('digite el primer numero: '))
    b = int(input('digite el primer numero: '))
    if  a == b: # modificamos
        raise NumerosIgualesExcepciones ('son iguales')
    resultado = a / b
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:
    print(f'Exception - ocurrio un error: {type(e)}')
else:
    print('no se arrojo ninguna excepcion')

finally: # siempre se va a ejecutar
    print('ejecucion de este bloque finally')

print(f'el resultado es: {resultado}')
print('seguimos...')'''

'''

#codigo Andy---------------------------------------------------------
from NumerosIgualesExcepciones import NumerosIgualesExcepciones
resultado = None

resultado = None

try:
    a = int (input('Digite el primer número: '))
    b = int (input('Digite el primer número: '))

    if a == b:
        raise NumerosIgualesExcepciones('Son números iguales')
    resultado = a / b
except TypeError as e:
    print(f'TypeError - ocurrió un error: {type(e)}')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error {type (e)}')

except Exception as e:
    print(f'Exception - Ocurrió un error: {type (e)}')

else:
    print(f'No se arrojo ninguna excepción')

finally:
    print("Ejecución de este bloque finally")

print(f'El resultado es {resultado}')
print('seguimos...') 

#--------------------------------------------------------------------
'''

from NumerosIgualesException import NumerosIgualesException
# Un error o excepcion es cuando nuestro codigo termina de manera abrupta o da error
resultado = None  # aca indicamos que la variable no tiene ningun valor


try:
    a = int (input("digite numero:"))
    b = int(input("digite otro numero:"))
    if a==b:
        raise NumerosIgualesException("son numeros iguales")
    #resultado = a/b

except TypeError as e:
    print(f"typerror -error fatal{type(e)}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError-error fatal {e}")
except Exception as e: #excepcion mas generica(clase padre-va al final del bloque)
    print(f"Exception -ocurrio un error, {e}")
else:
    print("No se arrojo ninguna excepcion, todo esta ok")
finally:
    print("gracias por utilizar este programa")
print(f"el resultado es: {resultado}")
print(f"seguimos ...")

