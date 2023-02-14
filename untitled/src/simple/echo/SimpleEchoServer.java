package simple.echo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.ServerSocket;
import java.io.IOException;
public class SimpleEchoServer {
    public static void main(String[] args) {
        // BufferedReader br = null;  // try -with 안쓰면 이렇게 하고 finally에서 close()해야함
        // PrintWriter pit = null;
        try (ServerSocket serverSocket = new ServerSocket(6000)) {
            Object connection;
            System.out.println("연결을 기다리는 중 ..........");
            Socket clientSocket = serverSocket.accept();
            System.out.println("클라이언트가 연결되었습니다. ");

            try (BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));  // client 소켓에서 getinputstream으로 가져옴
                 PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {  // autoflush: 버퍼 자동으로 비워주는 것
                String line;
                while ((line = br.readLine()) != null) {
                    System.out.println("클라이언트로 부터 받은 메세지: " + line);
                    out.println(line);
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            } //finally {
            //  br.close();
            //}
        } catch (IOException ex) {
            // Handle exceptions
        }
    }
}