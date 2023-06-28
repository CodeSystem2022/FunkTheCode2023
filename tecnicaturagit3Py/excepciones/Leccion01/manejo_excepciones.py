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

