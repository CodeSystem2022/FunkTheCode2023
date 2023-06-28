
package domain;

public enum TipoEscritura {
    CLASICO("Escritura a mano"),
    MODERNO("Escritura digital");
    
    private final String descripcion;
    
    private TipoEscritura(String descripcion){//cosntructor
        this.descripcion = descripcion;
    }
    
    //metodo get
    public String getDescripcion() {
        return this.descripcion;
    }
}
