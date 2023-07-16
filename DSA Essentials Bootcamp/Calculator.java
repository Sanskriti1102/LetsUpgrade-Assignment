import java.util.*;

public class Calculator {

    public static void main(String[] args) {
        System.out.println("<---Welcome to application !!--->");
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println(
                    "Calculator Menu: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\nEnter Your Choice:");
            int choice = sc.nextInt();

            if (choice == 5) {
                System.out.println("Exit from Program !!");
                break;
            }
            if (choice > 5 || choice < 1) {
                System.out.println("Wrong choice!!");
                continue;
            }

            System.out.println("\nEnter the first number, a:");
            int first = sc.nextInt();
            System.out.println("\nEnter the second number, b:");
            int second = sc.nextInt();

            int res = 0;

            switch (choice) {
                case 1:
                    res = first + second;
                    break;
                case 2:
                    res = first - second;
                    break;
                case 3:
                    res = first * second;
                    break;
                case 4:
                    res = first / second;
                    break;
                case 5:
                    ;
                    break;
                default:
                    System.out.println("Wrong choice!!");
                    break;
            }
            System.out.println("The Result is : " + res);

        }
    }

}
