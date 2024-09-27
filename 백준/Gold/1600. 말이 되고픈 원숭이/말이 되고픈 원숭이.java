import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static int K, N, M;
	private static int[][] board;
	private static boolean[][][] check;
	private static int[][] delta = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
	private static int[][] horse = { { -1, -2 }, { -2, -1 }, { -2, 1 }, { -1, 2 }, { 1, 2 }, { 2, 1 }, { 2, -1 }, { 1, -2 } };

	private static int dfs() {
		Queue<int[]> q = new ArrayDeque<>();
		q.add(new int[] {0, 0, 0, 0}); // y, x, 이동 횟수, 말 움직임 횟수
		int res = Integer.MAX_VALUE;
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			
			if (now[0] == N-1 && now[1] == M-1) {
				res = Math.min(res,  now[2]);
			}
			
			for (int[] d : delta) {
				int ny = now[0] + d[0];
				int nx = now[1] + d[1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < M && board[ny][nx] == 0 && !check[ny][nx][now[3]]) {
					check[ny][nx][now[3]] = true;
					q.add(new int[] {ny, nx, now[2]+1, now[3]});
				}
			}
			
			if (now[3] == K) {
				continue;
			}
			
			for (int[] h : horse) {
				int ny = now[0] + h[0];
				int nx = now[1] + h[1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < M && board[ny][nx] == 0 && !check[ny][nx][now[3]+1]) {
					check[ny][nx][now[3]+1] = true;
					q.add(new int[] {ny, nx, now[2]+1, now[3]+1});
				}
			}
		}
		
		return res;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());
		StringTokenizer size = new StringTokenizer(br.readLine());
		M = Integer.parseInt(size.nextToken());
		N = Integer.parseInt(size.nextToken());

		board = new int[N][M];
		check = new boolean[N][M][K+1];

		for (int i = 0; i < N; i++) {
			StringTokenizer line = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(line.nextToken());
			}
		}
		
		for (int k = 0; k < K+1; k++) {
			check[0][0][k] = true;
		}
		
		int res = dfs();
		
		if (res == Integer.MAX_VALUE) {
			res = -1;
		}
		
		System.out.println(res);
	}

}