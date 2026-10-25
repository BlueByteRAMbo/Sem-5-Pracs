import java.io.*;
import java.net.*;

public class CalculatorClient {
    public static void main(String[] args) {
        try (
            Socket socket = new Socket("127.0.0.1", 5002);
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in))
        ) {
            System.out.println("TCP Calculator");
            System.out.println("Operations: add, subtract, multiply, divide");
            System.out.println("For factorial, enter: factorial number");
            System.out.println("Example: add 10 5");

            System.out.print("Enter operation: ");
            String request = keyboard.readLine();

            output.println(request);

            String result = input.readLine();
            System.out.println("Result from server: " + result);

        } catch (IOException e) {
            System.out.println("Client error: " + e.getMessage());
        }
    }
}
