class Worker extends Thread{
    public void run(){
        try {
            for(int i = 0; i < 5; i++) {
                System.out.println("작업 쓰레드 : " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
        }
    }
}

public class ThreadHomework {
    public static void main(String[] args) {
        int alphabet = 'a';
        Worker worker = new Worker();
        worker.start();
        try {
            while (worker.isAlive()){
                System.out.println("메인 쓰레드 : " + (char)alphabet++);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
        }
    }
}
