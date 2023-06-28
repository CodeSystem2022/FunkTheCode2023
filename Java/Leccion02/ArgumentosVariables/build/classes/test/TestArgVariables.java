// public class ArgumentosVariables {
//     public static void main(String[] args) {

//         mostrarLibros("La Odisea");
//         mostrarLibros("1984", "Rebelión en la granja");
//         mostrarLibros("Cien años de soledad", "Crónica de una muerte anunciada", "El amor en los tiempos del cólera");


//         saludarPersonas("Juan", "María");
//         saludarPersonas("Pedro", "Ana", "Luisa");
//         saludarPersonas("Carlos", "Laura", "Andrés", "Marcela");


//         listarAnimales("Perro");
//         listarAnimales("Gato", "León");
//         listarAnimales("Elefante", "Jirafa", "Tigre", "Cebra");

//         testMostrarLibros();
//         testSaludarPersonas();
//         testListarAnimales();
      
//     }

//     public static void mostrarLibros(String... libros) {
//         System.out.println("Libros:");
//         for (String libro : libros) {
//             System.out.println(libro);
//         }
//         System.out.println();
//     }

//     public static void saludarPersonas(String... nombres) {
//         System.out.println("Saludos:");
//         for (String nombre : nombres) {
//             System.out.println("Hola, " + nombre + "!");
//         }
//         System.out.println();
//     }

//     public static void listarAnimales(String... animales) {
//         System.out.println("Animales:");
//         for (String animal : animales) {
//             System.out.println(animal);
//         }
//         System.out.println();
//     }
//     public static void testMostrarLibros() {
//         System.out.println("Probando método mostrarLibros():");
//         ArgumentosVariables.mostrarLibros("Libro 1", "Libro 2", "Libro 3");
//         ArgumentosVariables.mostrarLibros("Libro A", "Libro B");
//         ArgumentosVariables.mostrarLibros();
//         System.out.println();
//     }

//     public static void testSaludarPersonas() {
//         System.out.println("Probando método saludarPersonas():");
//         ArgumentosVariables.saludarPersonas("Juan", "María", "Pedro");
//         ArgumentosVariables.saludarPersonas("Ana");
//         ArgumentosVariables.saludarPersonas();
//         System.out.println();
//     }

//     public static void testListarAnimales() {
//         System.out.println("Probando método listarAnimales():");
//         ArgumentosVariables.listarAnimales("Perro", "Gato", "León", "Elefante");
//         ArgumentosVariables.listarAnimales("Tigre");
//         ArgumentosVariables.listarAnimales();
//         System.out.println();
//     }
// }
  
// }

public class ArgumentosVariables {
    public static void main(String[] args) {

        mostrarLibros("La Odisea");
        mostrarLibros("1984", "Rebelión en la granja");
        mostrarLibros("Cien años de soledad", "Crónica de una muerte anunciada", "El amor en los tiempos del cólera");


        saludarPersonas("Juan", "María");
        saludarPersonas("Pedro", "Ana", "Luisa");
        saludarPersonas("Carlos", "Laura", "Andrés", "Marcela");


        listarAnimales("Perro");
        listarAnimales("Gato", "León");
        listarAnimales("Elefante", "Jirafa", "Tigre", "Cebra");

        testMostrarLibros();
        testSaludarPersonas();
        testListarAnimales();
      
    }

    public static void mostrarLibros(String... libros) {
        System.out.println("Libros:");
        for (String libro : libros) {
            System.out.println(libro);
        }
        System.out.println();
    }

    public static void saludarPersonas(String... nombres) {
        System.out.println("Saludos:");
        for (String nombre : nombres) {
            System.out.println("Hola, " + nombre + "!");
        }
        System.out.println();
    }

    public static void listarAnimales(String... animales) {
        System.out.println("Animales:");
        for (String animal : animales) {
            System.out.println(animal);
        }
        System.out.println();
    }
    public static void testMostrarLibros() {
        System.out.println("Probando método mostrarLibros():");
        ArgumentosVariables.mostrarLibros("Libro 1", "Libro 2", "Libro 3");
        ArgumentosVariables.mostrarLibros("Libro A", "Libro B");
        ArgumentosVariables.mostrarLibros();
        System.out.println();
    }

    public static void testSaludarPersonas() {
        System.out.println("Probando método saludarPersonas():");
        ArgumentosVariables.saludarPersonas("Juan", "María", "Pedro");
        ArgumentosVariables.saludarPersonas("Ana");
        ArgumentosVariables.saludarPersonas();
        System.out.println();
    }

    public static void testListarAnimales() {
        System.out.println("Probando método listarAnimales():");
        ArgumentosVariables.listarAnimales("Perro", "Gato", "León", "Elefante");
        ArgumentosVariables.listarAnimales("Tigre");
        ArgumentosVariables.listarAnimales();
        System.out.println();
    }
}
  
}
