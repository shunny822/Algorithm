import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int N;
	static char[][] picture;
	static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	
	private static void normalView(int y, int x, boolean[][] check) {
		Queue<int[]> q = new LinkedList<>();
		int[] start = {y, x};
		q.add(start);
		check[y][x] = true;
		char target = picture[y][x];
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int ny = now[0] + delta[i][0];
				int nx = now[1] + delta[i][1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < N && !check[ny][nx] && picture[ny][nx] == target) {
					check[ny][nx] = true;
					int[] next = {ny, nx};
					q.add(next);
				}
			}
		}
	}
	
	private static void colorWeakView(int y, int x, boolean[][] check) {
		Queue<int[]> q = new LinkedList<>();
		int[] start = {y, x};
		q.add(start);
		check[y][x] = true;
		ArrayList<Character> target = new ArrayList<>();
		
		if (picture[y][x] == 'R' || picture[y][x] == 'G') {
			target.add('R');
			target.add('G');
		} else {
			target.add('B');
		}
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int ny = now[0] + delta[i][0];
				int nx = now[1] + delta[i][1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < N && !check[ny][nx] && target.contains(picture[ny][nx])) {
					check[ny][nx] = true;
					int[] next = {ny, nx};
					q.add(next);
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		picture = new char[N][N];
		
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			
			for (int j = 0; j < N; j++) {
				picture[i][j] = line.charAt(j);
			}
		}
		
		boolean[][] check = new boolean[N][N];
		int normal = 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!check[i][j]) {
					normalView(i, j, check);
					normal++;
				}
			}
		}
		
		check = new boolean[N][N];
		int colorWeak = 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!check[i][j]) {
					colorWeakView(i, j, check);
					colorWeak++;
				}
			}
		}
		
		System.out.println(normal + " " + colorWeak);
	}

}