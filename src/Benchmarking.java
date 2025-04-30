import java.util.Random;

public class Benchmarking {
    private MetodosOrdenamiento mOrdenamiento;
    public Benchmarking(){
        long currentMills = System.currentTimeMillis();
        long currentNano = System.nanoTime();
        System.out.println(currentMills);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);

        Runnable tarea = () -> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMillis = medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNanos = medirConNanoTime(tarea);

        System.out.println("Tiempo en milisegundos: "+tiempoDuracionMillis);
        System.out.println("Tiempo en nanosegundos: "+tiempoDuracionNanos);
    }

    private int [] generarArregloAleatorio(int tamaño){
        Random random = new Random();
        int [] array = new int[tamaño];
        for (int i = 0; i < tamaño; i++){
            array[i]=random.nextInt()*100000;
        }
        return array;
    }

    public double medirConCurrentTimeMiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) /1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        double tiempoSegundos = (fin - inicio) /1000000000.0;
        return tiempoSegundos;
    }
}
