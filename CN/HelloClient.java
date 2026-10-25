import java.io.*;
import java.net.*;

public class HelloClient {
    public static void main(String[] args) {
        try (
            Socket socket = new Socket("127.0.0.1", 5000);
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true)
        ) {
            output.println("Hello Server!");

            System.out.println("Server replied: " + input.readLine());

        } catch (IOException e) {
            System.out.println("Client error: " + e.getMessage());
        }
    }
}
