import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	private static int C, N;
	private static int[][] cost;
	
	private static int findMinCost() {
		int[] dp = new int[C+1];
		
		for (int i = 1; i < C+1; i++) {
			dp[i] = Integer.MAX_VALUE;
		}
		
		for (int j = 0; j < N; j++) {
			int c = cost[j][0];
			int customer = cost[j][1];
			
			for (int i = 1; i < C+1; i++) {
				if (customer < i) {
					dp[i] = Math.min(dp[i], dp[i-customer] + c);
				} else {
					dp[i] = Math.min(dp[i], c);
				}
			}
		}
		
		return dp[C];
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer nums = new StringTokenizer(br.readLine());
		C = Integer.parseInt(nums.nextToken());
		N = Integer.parseInt(nums.nextToken());
		cost = new int[N][2];
		
		for (int i = 0; i < N; i++) {
			nums = new StringTokenizer(br.readLine());
			int cityCost = Integer.parseInt(nums.nextToken());
			int customer = Integer.parseInt(nums.nextToken());
			
			cost[i] = new int[] {cityCost, customer};
		}
		
		System.out.println(findMinCost());
	}

}