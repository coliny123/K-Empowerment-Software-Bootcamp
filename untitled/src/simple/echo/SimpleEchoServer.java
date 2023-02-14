package simple.echo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.ServerSocket;
import java.io.IOException;
import java.util.Objects;
import java.util.function.Supplier;
import java.util.stream.Stream;

public class SimpleEchoServer {
    public static void main(String[] args) {
        System.out.println("에코 서버 시작됨");
        try (ServerSocket serverSocket = new ServerSocket(9900)) {
            System.out.println("클라이언트 접속 대기 중.....");
            Socket clientSocket = serverSocket.accept();  // 접속 대기
            System.out.println("클라이언트 접속됨.");

            try (
                    BufferedReader br = new BufferedReader(
                            new InputStreamReader(clientSocket.getInputStream()));
                    PrintWriter pw =
                            new PrintWriter(clientSocket.getOutputStream(), true))
            {
                Stream.generate(()-> {
                    try {
                        return br.readLine();
                    } catch (IOException ex) {
                        return null;
                    }
                }).peek(text -> {  // IED가 map은 쓸모없는 return한다고 생각해서 peek으로 변경해줌
                    System.out.println("클라이언트로 부터 받은 메세지 : " + text);  // while문에서 line의 역할을 함
                    pw.println(text);
                }).allMatch(Objects::nonNull);  // :: 참조할 때 쓰는 기호
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        catch (IOException ex) {
            System.out.println("접속 실패!");
        }
    }
}