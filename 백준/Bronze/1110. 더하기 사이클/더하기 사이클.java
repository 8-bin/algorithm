import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int count;

        if (N < 10) {
            N *= 10;
        }

        count = cycleCount(N);
        System.out.println(count);
    }

    public static int cycleCount(int N){
        int count = 0;
        int num = N;

        do {
            // 십의 자리와 일의 자리를 구한다.
            int tens = num / 10;
            int ones = num % 10;

            // 새로운 수를 만든다.
            num = (ones * 10) + ((ones + tens) % 10);

            // 사이클의 카운트를 측정한다.
            count++;
        } while (num != N);

        return count;
    }
}