
package mundoPC;

import ar.com.system2023.mundopc.*;

    public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); // IMPORTAR LA CLASE
        Teclado tecladoHP = new Teclado("bluetooth", "HP");
        Raton ratonHP = new Raton("bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //creamos otros objetos de diferencte marca
        Monitor monitorGamer = new Monitor("Gamer", 32); 
        Teclado tecladoGamer = new Teclado("bluetooth", "Gamer");
        Raton ratonGamer = new Raton("bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Orden orden1 = new Orden(); // inicializamos el arreglo vacio
        Orden orden2 = new Orden(); // una nueva lista para el objeto orden2

        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora computadoraVarias = new Computadora("computadora de diferentes marcas", monitorHP, tecladoGamer,ratonHP);
        orden2.agregarComputadora(computadoraVarias);
        
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
        //crear mas objetos de tipo computadora con todos sus elementos
        //completar en el orden1 que llegue a los 10 elementos
        //probar de esta manera los metodos al maximo rendimiento
    
        
    }
}
