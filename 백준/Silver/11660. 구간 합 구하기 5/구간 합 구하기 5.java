import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static StringBuilder sb = new StringBuilder();
	static int[][] arr;
	
	static void acc() {
		for (int i = 1; i < N+1; i++) {
			for (int j = 1; j < N+1; j++) {
				arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1];
			}
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer size = new StringTokenizer(br.readLine());
		N = Integer.parseInt(size.nextToken());
		M = Integer.parseInt(size.nextToken());
		arr = new int[N+1][N+1];
		
		for (int i = 1; i < N+1; i++) {
			StringTokenizer line = new StringTokenizer(br.readLine());
			
			for (int j = 1; j < N+1; j++) {
				arr[i][j] = Integer.parseInt(line.nextToken());
			}
		}
		
		acc();
		
		for (int i = 0; i < M; i++) {
			StringTokenizer position = new StringTokenizer(br.readLine());
			int y1 = Integer.parseInt(position.nextToken());
			int x1 = Integer.parseInt(position.nextToken());
			int y2 = Integer.parseInt(position.nextToken());
			int x2 = Integer.parseInt(position.nextToken());
			
			sb.append(arr[y2][x2] - arr[y2][x1-1] - arr[y1-1][x2] + arr[y1-1][x1-1]).append("\n");
		}
		
		System.out.println(sb.toString());
	}

}