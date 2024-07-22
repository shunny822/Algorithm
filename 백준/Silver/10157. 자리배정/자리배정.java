import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().split(" ");
		int[] xy = new int[2];
		xy[0] = Integer.parseInt(input[0]);
		xy[1] = Integer.parseInt(input[1]);

		int k = Integer.parseInt(br.readLine());
		
		if (k > xy[0] * xy[1]) {
			System.out.println(0);
		} else {
			boolean[][] check = new boolean[xy[0]][xy[1]];
			for (int i = 0; i < xy[0]; i++) {
				for (int j = 0; j < xy[1]; j++) {
					check[i][j] = false;
				}
			}
			
			int[] dx = { 0, 1, 0, -1 };
			int[] dy = { 1, 0, -1, 0 };
			int way = 0;
			int x = 0;
			int y = 0;
			int i = 1;
			check[0][0] = true;
			
			while (i < k) {
				int nx = x + dx[way];
				int ny = y + dy[way];
				
				if (ny < 0 || ny >= xy[1] || nx < 0 || nx >= xy[0] || check[nx][ny]) {
					way = (way+1)%4;
					continue;
				}
				
				check[nx][ny] = true;
				x = nx;
				y = ny;
				i++;
			}
			System.out.println((x+1) + " " + (y+1));
		}
	}

}