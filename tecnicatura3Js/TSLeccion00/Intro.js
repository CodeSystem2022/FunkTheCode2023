class IntegrantesFunkTheCode2023 {
  constructor() 
  {
    this.nombresApellidos = 
      [
      "Nicolás Rizo Avellaneda",
      "Andrés Montes",
      "Danilo Profita",
      "María Bárbara Natasha Herrera",
      "Sebastián Bustamante",
      "Carla Fuschino",
      "Matias Diaz de Otazu",
      "Catriel Quintana"
    ];
  }

  imprimirIntegrantes() {
    this.nombresApellidos.forEach(nombreApellido => {
      
      const [nombre, apellido] = nombreApellido.split(" ");
      
      console.log("Nombre:", nombre);
      
      console.log("Apellido:", apellido);
      
      console.log("");
      
    });
  }
}

const integrantes = new IntegrantesFunkTheCode2023();

integrantes.imprimirIntegrantes();
