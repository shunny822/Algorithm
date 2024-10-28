import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	private static int N, res;
	private static int[][] list;
	
	private static void findMaxLength() {
		int[] dp = new int[N];
		
		for (int i = 0; i < N; i++) {
			dp[i] = 1;
			
			for (int j = 0; j < i; j++) {
				if (list[i][1] > list[j][1]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
				}
			}
			
			res = Math.max(res, dp[i]);
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		res = 0;
		list = new int[N][2];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer nums = new StringTokenizer(br.readLine());
			list[i] = new int[] {Integer.parseInt(nums.nextToken()), Integer.parseInt(nums.nextToken())};
		}
		
		Arrays.sort(list, (o1, o2) -> {
			return o1[0] - o2[0];
		});
		
		findMaxLength();
		System.out.println(N-res);
	}

}