import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String sNum = sc.nextLine();
        char[] cNum = sNum.toCharArray();
        int sum = 0;
        for(char c : cNum) {
            sum += (c - '0');
        }
        System.out.print(sum);
    }
}