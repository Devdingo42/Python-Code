import java.util.Scanner;

public class CountWords {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string >> ");
        String inputString = scanner.nextLine();
        scanner.close();
        
        int wordCount = countWords(inputString);
        System.out.println("There are " + wordCount + " words in the string");
    }

    private static int countWords(String inputString) {
        String separatorRegex = "[\\s.,;?!\\-]+";

        String[] words = inputString.split(separatorRegex);

        return words.length;
    }
}