
package test;

import domain.*;

public class testClaseObject {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("juan",5000);
        Empleado empleado2 = new Empleado("juan", 5000);
        
        if(empleado1 == empleado2){
            System.out.println("tienen la misma referencia en memoria");
        }
        else{
            System.out.println("tienen distinta referencia en memoria");
        }
        
        if (empleado1.equals(empleado2)){
            System.out.println("los objetos son iguales en contenido");
        }
        else{
            System.out.println("los objetos son distintos en contenido");
        }
        
        if(empleado1.hashCode() == empleado2.hashCode()){
            System.out.println("el valor hascode es igual");
        }
        else{
            System.out.println("el valor hascode es diferente");
        }
    }
}
