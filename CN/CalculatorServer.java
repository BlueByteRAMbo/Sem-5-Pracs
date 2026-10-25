
import java.io.*;
import java.net.*;

public class CalculatorServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5002)) {
            System.out.println("Calculator Server started. Waiting for client...");

            try (
                Socket socket = serverSocket.accept();
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true)
            ) {
                System.out.println("Client connected!");
                String request = input.readLine();
                String result;

                try {
                    String[] parts = request.split(" ");
                    String operation = parts[0];

                    if (operation.equalsIgnoreCase("factorial")) {
                        int number = Integer.parseInt(parts[1]);

                        if (number < 0 || number > 20) {
                            throw new IllegalArgumentException("Enter a number from 0 to 20.");
                        }

                        long factorial = 1;

                        for (int i = 1; i <= number; i++) {
                            factorial *= i;
                        }

                        result = String.valueOf(factorial);
                    } else {
                        double firstNumber = Double.parseDouble(parts[1]);
                        double secondNumber = Double.parseDouble(parts[2]);

                        switch (operation) {
                            case "add":
                                result = String.valueOf(firstNumber + secondNumber);
                                break;

                            case "subtract":
                                result = String.valueOf(firstNumber - secondNumber);
                                break;

                            case "multiply":
                                result = String.valueOf(firstNumber * secondNumber);
                                break;

                            case "divide":
                                if (secondNumber == 0) {
                                    throw new ArithmeticException("Cannot divide by zero.");
                                }

                                result = String.valueOf(firstNumber / secondNumber);
                                break;

                            default:
                                result = "Invalid operation.";
                        }
                    }
                } catch (Exception e) {
                    result = "Error: " + e.getMessage();
                }

                output.println(result);
                System.out.println("Request: " + request);
                System.out.println("Result: " + result);
            }
        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }
}
