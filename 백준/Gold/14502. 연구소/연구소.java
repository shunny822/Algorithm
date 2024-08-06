import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static void makeCombi(int idx, int before, int[] arr, int l, boolean[] check, ArrayList<int[]> combis) {
		if (idx == 3) {
			combis.add(Arrays.copyOf(arr, 3));
			return;
		}
		
		for (int i = before+1; i < l; i++) {
			if (!check[i]) {
				check[i] = true;
				arr[idx] = i;
				makeCombi(idx+1, i, arr, l, check, combis);
				check[i] = false;
			}
		}
	}
	
	private static int bfs(int[][] matrix, boolean[][] check, int N, int M) {
		int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		Queue<int[]> q = new LinkedList<>();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (matrix[i][j] == 2) {
					check[i][j] = true;
					int[] position = {i, j};
					q.add(position);
				}
			}
		}
		
		while (!q.isEmpty()) {
			int[] yx = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int ny = yx[0] + delta[i][0];
				int nx = yx[1] + delta[i][1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < M && matrix[ny][nx] == 0 && !check[ny][nx]) {
					check[ny][nx] = true;
					int[] position = {ny, nx};
					q.add(position);
				}
			}
		}
		
		int res = 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (matrix[i][j] == 0 && !check[i][j]) {
					res++;
				}
			}
		}
		
		return res;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]);
		int M = Integer.parseInt(input[1]);
		int[][] matrix = new int[N][M];
		ArrayList<int[]> blank = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			StringTokenizer line = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				int n = Integer.parseInt(line.nextToken());
				matrix[i][j] = n;
				
				if (n == 0) {
					int[] position = {i, j};
					blank.add(position);
				}
			}
		}
		
		int l = blank.size();
		boolean[] check = new boolean[l];
		int[] arr = new int[3];
		ArrayList<int[]> combis = new ArrayList<>();
		
		makeCombi(0, -1, arr, l, check, combis);
		
		int ans = 0;
		for (int[] combi : combis) {
			for (int idx : combi) {
				int[] position = blank.get(idx);
				matrix[position[0]][position[1]] = 1;
			}
			
			boolean[][] visited = new boolean[N][M];
			ans = Math.max(ans, bfs(matrix, visited, N, M));
			
			for (int idx : combi) {
				int[] position = blank.get(idx);
				matrix[position[0]][position[1]] = 0;
			}
		}
		
		System.out.println(ans);
   }

}