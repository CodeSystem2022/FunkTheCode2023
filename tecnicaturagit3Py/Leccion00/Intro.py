class IntegrantesFunkTheCode2023:
  
    def __init__(self):
        self.nombres_apellidos = 
        [
            "Nicolás Rizo Avellaneda",
            "Andrés Montes",
            "Danilo Profita",
            "María Bárbara Natasha Herrera",
            "Sebastián Bustamante",
            "Carla Fuschino",
            "Matias Diaz de Otazu",
            "Catriel Quintana"
        ]

    def imprimir_integrantes(self):
        for nombre_apellido in self.nombres_apellidos:
          
            nombre, apellido = nombre_apellido.split()
          
            print("Nombre:", nombre)
          
            print("Apellido:", apellido)
          
            print("")

integrantes = IntegrantesFunkTheCode2023()

integrantes.imprimir_integrantes()
