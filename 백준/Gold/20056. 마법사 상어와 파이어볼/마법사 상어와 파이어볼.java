import java.io.*;
import java.util.*;

public class Main {
	private static int N, M, K;
	private static ArrayList<int[]>[][] board;
	private static int[][] delta = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer nums = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(nums.nextToken());
		M = Integer.parseInt(nums.nextToken());
		K = Integer.parseInt(nums.nextToken());
		board = new ArrayList[N+1][N+1];
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				board[i][j] = new ArrayList<>();
			}
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer info = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(info.nextToken());
			int c = Integer.parseInt(info.nextToken());
			int m = Integer.parseInt(info.nextToken());
			int s = Integer.parseInt(info.nextToken());
			int d = Integer.parseInt(info.nextToken());
			
			board[r][c].add(new int[] {m, s, d});
		}
		
		for (int i = 0; i < K; i++) {
			moveBall();
			divide();
		}
		
		System.out.println(cntMass());
	}
	
	private static void moveBall() {
		ArrayList<int[]>[][] newBoard = new ArrayList[N+1][N+1];
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				newBoard[i][j] = new ArrayList<>();
			}
		}
		
		for (int y = 1; y <= N; y++) {
			for (int x = 1; x <= N; x++) {
				for (int[] info : board[y][x]) {
					int s = info[1] % N;
					int ny = y + s*delta[info[2]][0];
					int nx = x + s*delta[info[2]][1];
					
					if (ny < 1) {
						ny += N;
					} else if (ny > N) {
						ny -= N;
					}
					
					if (nx < 1) {
						nx += N;
					} else if (nx > N) {
						nx -= N;
					}
					
					newBoard[ny][nx].add(info);
				}
			}
		}
		
		board = newBoard;
	}
	
	private static void divide() {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (board[i][j].size() > 1) {
					int totalMass = 0;
					int totalSpeed = 0;
					boolean isOdd = false;
					boolean isEven = false;
					
					for (int[] info : board[i][j]) {
						totalMass += info[0];
						totalSpeed += info[1];
						
						if (info[2]%2 == 1) {
							isOdd = true;
						} else {
							isEven = true;
						}
					}
					
					int m = totalMass/5;
					int s = totalSpeed/board[i][j].size();
					ArrayList<int[]> newArr = new ArrayList<>();
					
					if (m > 0) {
						int startIdx = 1;
						
						if ((isOdd && !isEven) || (!isOdd && isEven)) {
							startIdx = 0;
						}
						
						for (int d = startIdx; d < 8; d += 2) {
							newArr.add(new int[] {m, s, d});
						}
					}
					
					board[i][j] = newArr;
				}
				
				
			}
		}
	}
	
	private static int cntMass() {
		int cnt = 0;
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				for (int[] ball : board[i][j]) {
					cnt += ball[0];
				}
			}
		}
		
		return cnt;
	}
}