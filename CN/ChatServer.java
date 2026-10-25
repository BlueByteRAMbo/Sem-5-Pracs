import java.io.*;
import java.net.*;

public class ChatServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5001)) {
            System.out.println("Chat Server started. Waiting for client...");

            try (
                Socket socket = serverSocket.accept();
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in))
            ) {
                System.out.println("Client connected!");
                System.out.println("Type 'exit' to end the chat.");

                while (true) {
                    String clientMessage = input.readLine();

                    if (clientMessage == null || clientMessage.equalsIgnoreCase("exit")) {
                        System.out.println("Client disconnected.");
                        break;
                    }

                    System.out.println("Client: " + clientMessage);

                    System.out.print("You: ");
                    String serverMessage = keyboard.readLine();

                    output.println(serverMessage);

                    if (serverMessage.equalsIgnoreCase("exit"))
                        break;
                }
            }
        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }
}
