import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.URL;
import java.net.URLConnection;
import java.net.UnknownHostException;

public class Main {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://www.google.com");
            URLConnection urlConnection = url.openConnection();  // 연결 객체 생성
            BufferedReader br = new BufferedReader(new
                    InputStreamReader(urlConnection.getInputStream()));  // 버퍼 객체에 담겨 한줄씩 가져옴
            String line;
            while ((line = br.readLine()) != null) {  // 여기서 한줄 한줄씩 꺼냄
                System.out.println(line);
            }
            br.close();
        } catch (IOException ex) {
            // Handle exceptions
        }
    }
}

