import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[][] array = new int[5][5];

		for (int i = 0; i < 5; i++) {
			String input = br.readLine();
			StringTokenizer st = new StringTokenizer(input);

			for (int j = 0; j < 5; j++) {
				array[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[] nums = new int[25];

		for (int i = 0; i < 5; i++) {
			String input = br.readLine();
			StringTokenizer st = new StringTokenizer(input);

			for (int j = 0; j < 5; j++) {
				nums[i*5 + j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < 5; i++) {
			removeNumber(nums[i], array);
		}
		
		for (int i = 5; i < 25; i++) {
			removeNumber(nums[i], array);
			int bingo = checkBingo(array);
			
			if (bingo >= 3) {
				System.out.println(i + 1);
				break;
			}
		}
	}
	
	private static void removeNumber(int n, int[][] array) {
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				if (array[i][j] == n) {
					array[i][j] = 0;
				}
			}
		}
	}
	
	private static int checkBingo(int[][] array) {
		int bingo = 0;
		for (int i = 0; i < 5; i++) {
			int cnt = 0;
			
			for (int j = 0; j < 5; j++) {
				if (array[i][j] == 0) {
					cnt++;
				} else {
					break;
				}
			}
			
			if (cnt == 5) {
				bingo++;
			}
		}
		
		for (int i = 0; i < 5; i++) {
			int cnt = 0;
			
			for (int j = 0; j < 5; j++) {
				if (array[j][i] == 0) {
					cnt++;
				} else {
					break;
				}
			}
			
			if (cnt == 5) {
				bingo++;
			}
		}
		
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (array[i][i] == 0) {
				cnt++;
			} else {
				break;
			}
		}
		
		if (cnt == 5) {
			bingo++;
		}
		
		cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (array[i][4-i] == 0) {
				cnt++;
			} else {
				break;
			}
		}
		
		if (cnt == 5) {
			bingo++;
		}
		
		return bingo;
	}

}