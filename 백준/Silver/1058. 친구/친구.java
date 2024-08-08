import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
	private static int N;
	private static int[][] arr;
	
	private static int cntFriends(int idx) {
		Set<Integer> friends = new HashSet<>();
		
		for (int i = 0; i < N; i++) {
			if (arr[idx][i] == 1) {
				friends.add(i);
				
				for (int j = 0; j < N; j++) {
					if (arr[i][j] == 1 && j != idx) {
						friends.add(j);
					}
				}
			}
		}
		return friends.size();
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			
			for (int j = 0; j < N; j++) {
				if (line.charAt(j) == 'Y' ) {
					arr[i][j] = 1;
				} else {
					arr[i][j] = 0;
				}
			}
		}
		
		int res = 0;
		
		for (int i = 0; i < N; i++) {
			res = Math.max(res, cntFriends(i));
		}
		
		System.out.println(res);
   }

}