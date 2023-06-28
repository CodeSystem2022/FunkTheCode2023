public class IntegrantesFunkTheCode2023 {
  
    private String[] nombresApellidos = 
    {
        "Nicolás Rizo Avellaneda",
        "Andrés Montes",
        "Danilo Profita",
        "María Bárbara Natasha Herrera",
        "Sebastián Bustamante",
        "Carla Fuschino",
        "Matias Diaz de Otazu",
        "Catriel Quintana"
    };

    public void imprimirIntegrantes() {
      
        for (String nombreApellido : nombresApellidos) 
          {
            String[] partes = nombreApellido.split(" ");
            String nombre = partes[0];
            String apellido = partes[1];
            System.out.println("Nombre: " + nombre);
            System.out.println("Apellido: " + apellido);
            System.out.println();
        }
    }

    public static void main(String[] args) {
        IntegrantesFunkTheCode2023 integrantes = new IntegrantesFunkTheCode2023();
      
        integrantes.imprimirIntegrantes();
    }
}
