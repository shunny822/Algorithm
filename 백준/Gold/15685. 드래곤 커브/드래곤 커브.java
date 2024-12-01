import java.io.*;
import java.util.*;

public class Main {
	private static boolean[][] arr = new boolean[101][101];
	private static int[][] delta = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
	
	private static void makeDragonCurve(int x, int y, int d, int G) {
		int endY = y+delta[d][0];
		int endX = x+delta[d][1];
		arr[y][x] = true;
		arr[endY][endX] = true;
		
		List<Integer> curve = new ArrayList<>();
		curve.add(d);
		
		for (int g = 0; g < G; g++) {
			int l = curve.size();
			
			for (int i = l-1; i >= 0; i--) {
				int nd = (curve.get(i)+1) % 4;
				endY += delta[nd][0];
				endX += delta[nd][1];
				
				arr[endY][endX] = true;
				curve.add(nd);
			}
		}
	}
	
	private static int countBlock() {
		int cnt = 0;
		
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (arr[i][j] && arr[i+1][j] && arr[i][j+1] && arr[i+1][j+1]) {
					cnt++;
				}
			}
		}
		
		return cnt;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < N; i++) {
			StringTokenizer nums = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(nums.nextToken());
			int y = Integer.parseInt(nums.nextToken());
			int d = Integer.parseInt(nums.nextToken());
			int G = Integer.parseInt(nums.nextToken());
			
			makeDragonCurve(x, y, d, G);
		}
		
		System.out.println(countBlock());
	}

}