import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static int[][] dp = new int[5][5];
	
	private static int calcPower(int foot, int next) {
		if (foot == 0) {
			return 2;
		} else if (foot == next) {
			return 1;
		} else if (Math.abs(foot-next) == 2) {
			return 4;
		}
		return 3;
	}
	
	private static void findMinPower(int next) {
		int[][] newDp = new int[5][5];
		
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (dp[i][j] > 0 && i != next) {
					if (newDp[i][next] > 0) {
						newDp[i][next] = Math.min(newDp[i][next], dp[i][j] + calcPower(j, next));
					} else {
						newDp[i][next] = dp[i][j] + calcPower(j, next);
					}
					newDp[next][i] = newDp[i][next];
				}
			}
		}
		
		dp = newDp;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer nums = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(nums.nextToken());
		
		dp[0][n] = 2;
		dp[n][0] = 2;
		
		while(true) {
			n = Integer.parseInt(nums.nextToken());
			
			if (n == 0) {
				break;
			}
			
			findMinPower(n);
		}
		
		int res = Integer.MAX_VALUE;
		
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (dp[i][j] > 0) {
					res = Math.min(res, dp[i][j]);
				}
			}
		}
		
		System.out.println(res);
	}

}