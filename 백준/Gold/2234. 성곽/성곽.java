import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static int N, M, cnt;
	private static int[][] board;
	private static boolean[][] check;
	private static ArrayList<Integer> roomSize = new ArrayList<>();
	private static ArrayList<int[]> roomStart = new ArrayList<>();
	private static int[][] delta = { { 0, -1 }, { -1, 0 }, { 0, 1 }, { 1, 0 } }; // 서 북 동 남
	private static int res = 0;

	private static void bfs(int i, int j) {
		roomStart.add(new int[] {i, j});
		Queue<int[]> q = new ArrayDeque<>();
		q.add(new int[] {i, j});
		check[i][j] = true;
		int size = 0;
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			
			for (int idx = 0; idx < 4; idx++) {
				int[] d = delta[idx];
				int ny = now[0] + d[0];
				int nx = now[1] + d[1];
				
				if ((board[now[0]][now[1]] & (1 << idx)) == 0 && ny >= 0 && ny < N && nx >= 0 && nx < M && !check[ny][nx]) {
					check[ny][nx] = true;
					q.add(new int[] {ny, nx});
				}
			}
			
			board[now[0]][now[1]] = cnt;
			size++;
		}
		
		roomSize.add(size);
	}
	
	private static void exploreRoom(int roomIdx) {
		int[] start = roomStart.get(roomIdx);
		Queue<int[]> q = new ArrayDeque<>();
		q.add(start);
		boolean[][] visited = new boolean[N][M];
		visited[start[0]][start[1]] = true;
		int room = roomSize.get(roomIdx);
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			
			for (int idx = 0; idx < 4; idx++) {
				int[] d = delta[idx];
				int ny = now[0] + d[0];
				int nx = now[1] + d[1];
				
				if (ny >= 0 && ny < N && nx >= 0 && nx < M && !visited[ny][nx]) {
					visited[ny][nx] = true;
					
					if (board[ny][nx] == roomIdx) {
						q.add(new int[] {ny, nx});
					} else {
						res = Math.max(res, room + roomSize.get(board[ny][nx]));
					}
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer nums = new StringTokenizer(br.readLine());
		M = Integer.parseInt(nums.nextToken());
		N = Integer.parseInt(nums.nextToken());
		cnt = 0; // 방의 개수

		board = new int[N][M];
		check = new boolean[N][M];

		for (int i = 0; i < N; i++) {
			StringTokenizer line = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(line.nextToken());
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!check[i][j]) {
					bfs(i, j);
					cnt++;
				}
			}
		}
		
		for (int i = 0; i < cnt; i++) {
			exploreRoom(i);
		}
		
		System.out.println(cnt);
		System.out.println(Collections.max(roomSize));
		System.out.println(res);
	}

}