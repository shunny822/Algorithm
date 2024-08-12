import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[][] board;
	static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	
	private static boolean isEmpty() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (board[i][j] == 1) {
					return false;
				}
			}
		}
		return true;
	}
	
	private static int melt() {
		Queue<int[]> q = new LinkedList<>();
		int[] start = {0, 0};
		q.add(start);
		
		boolean[][] check = new boolean[N][M];
		check[0][0] = true;
		int cnt = 0;
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int ny = now[0] + delta[i][0];
				int nx = now[1] + delta[i][1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < M && !check[ny][nx]) {
					check[ny][nx] = true;
					
					if (board[ny][nx] == 1) {
						board[ny][nx] = 0;
						cnt++;
					} else {
						int[] next = {ny, nx};
						q.add(next);
					}
				}
			}
		}
		
		return cnt;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer numbers = new StringTokenizer(br.readLine());
		N = Integer.parseInt(numbers.nextToken());
		M = Integer.parseInt(numbers.nextToken());
		board = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer line = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(line.nextToken());
			}
		}
		
		int hour = 0;
		int lastCheese = 0;
		
		while (!isEmpty()) {
			lastCheese = melt();
			hour++;
		}
		
		System.out.println(hour + "\n" + lastCheese);
	}

}