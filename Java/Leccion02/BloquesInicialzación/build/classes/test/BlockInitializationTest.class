public class BlockInitializationTest {

    private static int staticVariable;

    private int instanceVariable;

    static {
        staticVariable = 10;
        System.out.println("Bloque de inicialización estático ejecutado.");
    }

    {
        instanceVariable = 20;
        System.out.println("Bloque de inicialización de instancia ejecutado.");
    }

    public BlockInitializationTest() {
        System.out.println("Constructor ejecutado.");
    }

    public void printValues() {
        System.out.println("staticVariable = " + staticVariable);

        System.out.println("instanceVariable = " + instanceVariable);
    }

    public static void main(String[] args) {
        BlockInitializationTest test = new BlockInitializationTest();
        test.printValues();
    }
}
