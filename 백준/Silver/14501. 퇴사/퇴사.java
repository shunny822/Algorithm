import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String strN = br.readLine();
		int n = Integer.parseInt(strN);
		int[][] schedule = new int[n][2];

		for (int i = 0; i < n; i++) {
			String input = br.readLine();
			StringTokenizer st = new StringTokenizer(input);
			
			schedule[i][0] = Integer.parseInt(st.nextToken());
			schedule[i][1] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[n+1];
		
		for (int i = 0; i < n+1; i++) {
			dp[i] = 0;
		}
		
		for (int i = 1; i < n+1; i++) {
			int endDay = i + schedule[i-1][0] - 1;
			
			if (endDay <= n) {
				dp[endDay] = Math.max(Arrays.stream(Arrays.copyOfRange(dp, 0, i)).max().getAsInt() + schedule[i-1][1], dp[endDay]);
			}
		}
        
		System.out.println(Arrays.stream(dp).max().getAsInt());
	}
}