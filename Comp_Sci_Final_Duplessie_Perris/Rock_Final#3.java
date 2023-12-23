import java.util.Scanner;

public class Rock {
    public static void main(String[] args) {
        String personPlay; // User's play -- "R", "P", or "S"
        String computerPlay = "U"; // Computer's play -- "R", "P", or "S"
        int computerInt; // Randomly generated number for computer play
        Scanner scan = new Scanner(System.in);

        for (int round = 1; round <= 10; round++) {
            System.out.print("Enter your play (R for Rock, P for Paper, or S for Scissors): ");
            personPlay = scan.nextLine().toUpperCase(); // Make player's play uppercase for ease of comparison

            // Ensure that the user's entry is one of the valid choices
            while (!personPlay.equals("R") && !personPlay.equals("P") && !personPlay.equals("S")) {
                System.out.println("Invalid input. Please enter R for Rock, P for Paper, or S for Scissors.");
                System.out.print("Enter your play (R for Rock, P for Paper, or S for Scissors): ");
                personPlay = scan.nextLine().toUpperCase();
            }

            // Generate computer's play (0, 1, 2). Use the Math.random() method
            computerInt = (int) (Math.random() * 3);

            // Translate computer's randomly generated play to string using a switch statement
            switch (computerInt) {
                case 0:
                    computerPlay = "R";
                    break;
                case 1:
                    computerPlay = "P";
                    break;
                case 2:
                    computerPlay = "S";
                    break;
            }

            // Print computer's play
            System.out.println("Computer play is " + computerPlay);

            // See who won. Use nested ifs instead of &&
            if (personPlay.equals(computerPlay)) {
                System.out.println("It's a tie!");
            } else if (personPlay.equals("R")) {
                if (computerPlay.equals("S")) {
                    System.out.println("Rock crushes scissors. You win!!");
                } else {
                    System.out.println("Paper covers rock. Computer wins!");
                }
            } else if (personPlay.equals("P")) {
                if (computerPlay.equals("R")) {
                    System.out.println("Paper covers rock. You win!!");
                } else {
                    System.out.println("Scissors cut paper. Computer wins!");
                }
            } else if (personPlay.equals("S")) {
                if (computerPlay.equals("P")) {
                    System.out.println("Scissors cut paper. You win!!");
                } else {
                    System.out.println("Rock crushes scissors. Computer wins!");
                }
            }
        }
    }
}