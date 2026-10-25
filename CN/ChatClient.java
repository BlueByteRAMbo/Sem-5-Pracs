import java.io.*;
import java.net.*;

public class ChatClient {
    public static void main(String[] args) {
        try (
            Socket socket = new Socket("127.0.0.1", 5001);
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in))
        ) {
            System.out.println("Connected to Chat Server!");
            System.out.println("Type 'exit' to end the chat.");

            while (true) {
                System.out.print("You: ");
                String clientMessage = keyboard.readLine();

                output.println(clientMessage);

                if (clientMessage == null ||
                    clientMessage.equalsIgnoreCase("exit")) {
                    break;
                }

                String serverMessage = input.readLine();

                if (serverMessage == null ||
                    serverMessage.equalsIgnoreCase("exit")) {
                    System.out.println("Server disconnected.");
                    break;
                }

                System.out.println("Server: " + serverMessage);
            }
        } catch (IOException e) {
            System.out.println("Client error: " + e.getMessage());
        }
    }
}
