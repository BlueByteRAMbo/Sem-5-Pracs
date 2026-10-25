import java.io.*;
import java.net.*;

public class HelloServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5000)) {
            System.out.println("Hello Server listening on port 5000; waiting for client...");

            try (
                Socket socket = serverSocket.accept();
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true)
            ) {
                System.out.println("Client says: " + input.readLine());
                output.println("Hello from the server! Message received.");
            }
        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }
}
