class NumerosIgualesExcepciones (Exception): # EXTIENDE DE LA CLASE
    def __init__(self, mensaje):
        self.message = mensaje