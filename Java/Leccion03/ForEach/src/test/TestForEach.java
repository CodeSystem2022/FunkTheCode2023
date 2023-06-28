package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
       int edades[] = {5, 9, 8,9};
        for (int edad: edades) { // sintaxis del foreach
            System.out.println("edad= "+ edad);
        }
        
        Persona personas[]= {new Persona("Juan"),new Persona("Carla"), new Persona("Beatriz")};
        
        //foreach
        for(Persona persona: personas){
            System.out.println("persona = " + persona);
        }
    }
}
