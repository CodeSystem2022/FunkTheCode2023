package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: " +Dias.LUNES);
        //indicarDiaSemana(Dias.JUEVES); // las enumeraciones se tratan como cadenas
        //no se deben itulizar comillas, se accede a travez de el operador de punto
    
        System.out.println("Continente nº. 1: " + Continentes.AFRICA +
                " \nNº. de paises en el 1ro. continente: " + Continentes.AFRICA.getPaises()+
                "\nNº. de habitantes en el 1ro. continente: "+Continentes.AFRICA.gethabitantes());
        
        System.out.println("\nContinente nº. 2: " + Continentes.EUROPA +
                " \nNº. de paises en el 2do. continente: " + Continentes.EUROPA.getPaises()+
                "\nNº. de habitantes en el 2do. continente: "+Continentes.EUROPA.gethabitantes());
        
        System.out.println("\nContinente nº. 3: " + Continentes.ASIA +
                " \nNº. de paises en el 3er. continente: " + Continentes.ASIA.getPaises()+
                "\nNº. de habitantes en el 3er. continente: "+Continentes.ASIA.gethabitantes());
        
        System.out.println("\nContinente nº. 4: " + Continentes.AMERICA +
                " \nNº. de paises en el 4to. continente: " + Continentes.AMERICA.getPaises()+
                "\nNº. de habitantes en el 4to. continente: "+Continentes.AMERICA.gethabitantes());
        
        System.out.println("\nContinente nº. 5: " + Continentes.OCEANICA +
                " \nNº. de paises en el 5to. continente: " + Continentes.OCEANICA.getPaises()+
                "\nNº. de habitantes en el 5to. continente: "+Continentes.OCEANICA.gethabitantes());
        
        
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;
            default:
                System.out.println("El dato ingresado es erroneo");
                break;
        }
    }
    
}
