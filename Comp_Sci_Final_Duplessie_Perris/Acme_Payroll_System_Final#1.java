import java.util.*;

public class ACMEPay {
    public static void main(String[] args) throws Exception 
    {
        int retire = 0;
        Scanner input = new Scanner(System.in);

        System.out.println("Please enter shift - 1 , 2 , or 3");
        int shift = input.nextInt();

        System.out.println("Please enter hours worked:");
        double hours = input.nextDouble();

        if (shift == 2 || shift == 3) {
            System.out.println("Do you want to participate in the retirement plan? (1 for Yes, 0 for No)");
            retire = input.nextInt();
        }

        double rate = payRate(shift);
        double gross = grossPay(rate, hours);

        System.out.println("Hours worked is " + hours);
        System.out.println("Shift is " + shift);
        System.out.println("Hourly pay rate is $" + rate);
        hoursBreakdown(rate, hours);
        retirementPay(shift, retire, gross);
    }

    public static double payRate(int shift) {
        double rate;
        switch (shift) {
            case 1:
                rate = 17.0;
                break;
            case 2:
                rate = 18.50;
                break;
            case 3:
                rate = 22.0;
                break;
            default:
                rate = 0.0;
                break;
        }
        return rate;
    }

    public static void hoursBreakdown(double rate, double hours) {
        double regularPay, overtimePay, totalPay;

        if (hours <= 40) {
            regularPay = hours * rate;
            overtimePay = 0.0;
        } else {
            regularPay = 40 * rate;
            overtimePay = (hours - 40) * 1.5 * rate;
        }

        totalPay = regularPay + overtimePay;

        System.out.println("Regular pay is " + regularPay);
        System.out.println("Overtime pay is " + overtimePay);
        System.out.println("Total pay is " + totalPay);
    }

    public static double grossPay(double rate, double hours) {
        double pay;
        if (hours <= 40) {
            pay = hours * rate;
        } else {
            pay = 40 * rate + (hours - 40) * 1.5 * rate;
        }
        return pay;
    }

    public static void retirementPay(int shift, int choice, double gross) {
        double retirementDeduction = 0.03 * gross;
        double netPay = gross - retirementDeduction;

        System.out.println("Retirement Deduction is " + retirementDeduction);
        System.out.println("Net Pay is " + netPay);
    }
}