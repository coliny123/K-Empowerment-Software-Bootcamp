import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ThreadPoolExecutor;

public class ThreadHomework {
    public static void main(String[] args) {
        int alphabet = 'a';
        ExecutorService exec = Executors.newCachedThreadPool();
        Runnable task = ()->{
            try {
                for (int i = 0; i < 5; i++){
                    System.out.println("작업 쓰레드 : " + i);
                    Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
            }
            exec.shutdown();
        };
        exec.execute(task);

        try {
            while (!exec.isShutdown()){
                System.out.println("메인 쓰레드 : " + (char)alphabet++);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
        }
    }
}
