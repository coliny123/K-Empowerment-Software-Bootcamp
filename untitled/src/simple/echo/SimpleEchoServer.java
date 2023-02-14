package simple.echo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.ServerSocket;
import java.io.IOException;


public class SimpleEchoServer implements Runnable {
    private static Socket clientSocket;

    public SimpleEchoServer(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }


    public static void main(String[] args) {
        System.out.println("Threaded Echo Server");
        try (ServerSocket serverSocket = new ServerSocket(6000)) {
            while (true) {
                System.out.println("Waiting for connection.....");
                clientSocket = serverSocket.accept();
                SimpleEchoServer tes = new SimpleEchoServer(clientSocket);
                new Thread(tes).start();  // Runable 인터페이스에서 implements 함
            }
        } catch (IOException ex) {
            // Handle exceptions
        }
        System.out.println("Threaded Echo Server Terminating");
    }
        @Override
        public void run () {
            System.out.println("Connected to client using [" + Thread.currentThread() + "]");
            try (BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {
                String inputLine;
                while ((inputLine = br.readLine()) != null) {
                    System.out.println("Client request [" + Thread.currentThread() + "]: " + inputLine);
                    out.println(inputLine);
                }
                System.out.println("Client [" + Thread.currentThread() + " connection terminated");
            } catch (IOException ex) {
                // Handle exceptions
            }
        }
}
