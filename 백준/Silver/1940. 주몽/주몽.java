import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// N(재료의 개수), M(갑옷이 되는 번호) 저장하기
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		// 재료 배열 저장하기
		int[] A = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < N ; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		// 재료 배열 정렬하기
		Arrays.sort(A);
		
		int count = 0;
		int i = 0; // A[0]
		int j = N-1; // A[N-1]
		
		while(i < j) {
			if(A[i] + A[j] < M) {
				i++;
			}else if(A[i] + A[j] > M) {
				j--;
			}else {
				count++;
				i++;
				j--;
			}
		}
		// count 출력하기
		System.out.println(count);
	}
}