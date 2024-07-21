import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[n+1];
		
		for (int i = 0; i < n+1; i++) {
			dp[i] = (int) 1e9;
		}

		dp[1] = 0;

		for (int i = 1; i < n+1; i++) {
			
			if (i*3 < n+1) {
				dp[i*3] = Math.min(dp[i] + 1, dp[i*3]);
			}
			if (i*2 < n+1) {
				dp[i*2] = Math.min(dp[i] + 1, dp[i*2]);
			}
			if (i+1 < n+1) {
				dp[i+1] = Math.min(dp[i] + 1, dp[i+1]);
			}
			
		}
		
		System.out.println(dp[n]);
	}

}