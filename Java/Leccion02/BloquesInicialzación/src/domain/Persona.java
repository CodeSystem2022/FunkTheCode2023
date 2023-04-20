package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{// bloque de inicializacion estatico
        System.out.println("ejecucion del bloque estatico");
        ++Persona.contadorPersonas;
       // idPersona = 10 ; no es estatituco un atributo, por eso tenemos un error
    }
    
    {//bloque de inicializacion NO estatico(cotexto dinamico)
        System.out.println("Ejecucion del bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++; // Incrementos el atributo
    }
    
    // los bloques de inicializacion se ejecutan antes del conductor
    public Persona(){
        System.out.println("Ejecucion del constructor");
    }
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
