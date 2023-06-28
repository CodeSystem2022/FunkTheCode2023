import java.util.ArrayList;
import java.util.List;

public class Autoboxing {
    private List<Integer> datos;

    public Autoboxing() 
    {
        datos = new ArrayList<>();
    }

    public void agregarDato(int valor) 
    {
        datos.add(valor);
    }

    public int obtenerDato(int indice) 
    {
        return datos.get(indice);
    }

    public int sumarDatos() 
    {
        int suma = 0;
        for (Integer valor : datos) {
            suma += valor;
        }
        return suma;
    }

    public static void main(String[] args) {
        Autoboxing autoboxing = new Autoboxing();
        
        autoboxing.agregarDato(10);
        autoboxing.agregarDato(5);
        autoboxing.agregarDato(7);
        autoboxing.agregarDato(3);
        autoboxing.agregarDato(12);
        
        int valor = autoboxing.obtenerDato(2);
        System.out.println("Valor en el índice 2: " + valor);
        
        int suma = autoboxing.sumarDatos();
        System.out.println("Suma de los datos: " + suma);
    }
}

// import java.util.ArrayList;
// import java.util.List;

// public class Autoboxing {
//     private List<Integer> datos;

//     public Autoboxing() {
//         datos = new ArrayList<>();
//     }

//     public void agregarDato(int valor) {
//         datos.add(valor);
//     }

//     public int obtenerDato(int indice) {
//         return datos.get(indice);
//     }

//     public int sumarDatos() {
//         int suma = 0;
//         for (Integer valor : datos) {
//             suma += valor;
//         }
//         return suma;
//     }

//     public static void main(String[] args) {
//         Autoboxing autoboxing = new Autoboxing();
        
//         // Agregar algunos datos aleatorios
//         autoboxing.agregarDato(10);
//         autoboxing.agregarDato(5);
//         autoboxing.agregarDato(7);
//         autoboxing.agregarDato(3);
//         autoboxing.agregarDato(12);
        
//         // Obtener el dato en el índice 2
//         int valor = autoboxing.obtenerDato(2);
//         System.out.println("Valor en el índice 2: " + valor);
        
//         // Calcular la suma de los datos
//         int suma = autoboxing.sumarDatos();
//         System.out.println("Suma de los datos: " + suma);
//     }
// }
