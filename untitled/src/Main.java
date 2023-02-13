import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;

public class Main {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new  // try(~~~~){} => 파이썬의 try-with-catch 구문처럼 실행되고 끝난다음 자동으로 메모리에서 사라짐
                ServerSocket(6000)){     // 원래 객체 사라질 때는 close() 를 선언해야 함
            Object connection;
            System.out.println("Waiting for connection.....");
            Socket clientSocket =
                    serverSocket.accept();
            System.out.println("Connected to client");
        } catch (IOException ex) {
            // Handle exceptions
        }
    }
}

