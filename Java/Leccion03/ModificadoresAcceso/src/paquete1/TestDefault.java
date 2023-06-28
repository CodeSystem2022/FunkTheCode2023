
package paquete1;

import paquete2.Clase4;

public class TestDefault {
    public static void main(String[] args) {
        ClaseHija2  claseh2 = new ClaseHija2();
        claseh2.atributoDefault = "cambio desde la prueba";
        System.out.println("claseh2 atributo default = " + claseh2.atributoDefault);
        
        Clase4 clase4 = new Clase4("Publico");
        System.out.println(clase4.getAtributoPrivate());
        clase4.setAtributoPrivate("cambio");
        System.out.println("clase4 = " +clase4.getAtributoPrivate());
   }
}
