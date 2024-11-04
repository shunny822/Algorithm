import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	private static int N;
	private static int[][] arr;
	private static int[][] dp;
	private static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	
	private static int findMaxPath(int y, int x) {
		int temp = 0;
		
		for (int[] d : delta) {
			int ny = y + d[0];
			int nx = x + d[1];
			
			if (ny >= 0 && ny < N && nx >= 0 && nx < N && arr[ny][nx] > arr[y][x]) {
				if (dp[ny][nx] == -1) {
					temp = Math.max(temp, findMaxPath(ny, nx));
				} else {
					temp = Math.max(temp, dp[ny][nx]);
				}
			}
		}
		
		dp[y][x] = temp + 1;
		return dp[y][x];
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		dp = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer nums = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(nums.nextToken());
				dp[i][j] = -1;
			}
		}
		
		int res = 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				res = Math.max(res, findMaxPath(i, j));
			}
		}
		
		System.out.println(res);
	}

}