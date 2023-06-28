
package domain;

public class Rectangulo extends FiguraGeometrica {
    //constructor
    public Rectangulo (String tipoFigura){
        super(tipoFigura);
    }
    
    @Override
    public void dibujar(){// implementando el metodo
        System.out.println("se imprime un : "+ this.getClass().getSimpleName());
    }
}
//Codigo de Matias Diaz de Otazu
/*
package domain;

public class Rectangulo extends FiguraGeometrica {
    //constructor
    public Rectangulo (String tipoFigura){
        super(tipoFigura);
    }
    
    @Override
    public void dibujar(){// implementando el metodo
        System.out.println("se imprime un : "+ this.getClass().getSimpleName());
    }
}
*/
