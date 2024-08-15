import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static StringBuilder sb = new StringBuilder();

	private static void makeSequence(int before, int idx, int[] arr, boolean[] check) {
		if (idx == M) {
			for (int n : arr) {
				sb.append(n + 1).append(" ");
			}
			sb.append("\n");
			return;
		}

		for (int i = before+1; i < N-M+idx+1; i++) {
			if (!check[i]) {
				check[i] = true;
				arr[idx] = i;
				makeSequence(i, idx + 1, arr, check);
				check[i] = false;
			}
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer input = new StringTokenizer(br.readLine());
		N = Integer.parseInt(input.nextToken());
		M = Integer.parseInt(input.nextToken());
		
		makeSequence(-1, 0, new int[M], new boolean[N]);
		System.out.println(sb.toString());
	}

}