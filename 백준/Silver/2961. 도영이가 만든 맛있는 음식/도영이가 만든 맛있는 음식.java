import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] tastes;
	
	static int findRecipe() {
		int res = Integer.MAX_VALUE;
		
		for (int i = 1; i < (1 << N); i++) {
			int sour = 1;
			int bitter = 0;
			
			for (int j = 0; j < N; j++) {
				if ((i & (1 << j)) != 0) {
					sour *= tastes[j][0];
					bitter += tastes[j][1];
				}
			}
			res = Math.min(res, Math.abs(sour - bitter));
		}
		return res;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		tastes = new int[N][2];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer numbers = new StringTokenizer(br.readLine());
			int[] taste = {Integer.parseInt(numbers.nextToken()), Integer.parseInt(numbers.nextToken())};
			tastes[i] = taste;
		}
		System.out.println(findRecipe());
	}

}