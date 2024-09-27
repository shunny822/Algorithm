import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static int L, R, C;
    private static int[] S, E;
    private static int[][][] board;
    private static boolean[][][] check;
    private static int[][] delta = {{-1, 0, 0}, {1, 0, 0}, {0, -1, 0}, {0, 1, 0}, {0, 0, -1}, {0, 0, 1}};

    private static int bfs() {
    	Queue<int[]> q = new ArrayDeque<>();
    	q.add(new int[] {S[0], S[1], S[2], 0});
    	check[S[0]][S[1]][S[2]] = true;
    	int res = 0;
    	
    	while (!q.isEmpty()) {
    		int[] now = q.poll();
    		
    		if (now[0] == E[0] && now[1] == E[1] && now[2] == E[2]) {
    			res = now[3];
    			break;
    		}
    		
    		for (int[] d : delta) {
    			int nz = now[0] + d[0];
    			int ny = now[1] + d[1];
    			int nx = now[2] + d[2];
    			
    			if (nz >= 0 && nz < L && ny >= 0 && ny < R && nx >= 0 && nx < C && !check[nz][ny][nx] && board[nz][ny][nx] == 0) {
    				check[nz][ny][nx] = true;
    				q.add(new int[] {nz, ny, nx, now[3]+1});
    			}
    		}
    	}
    	
        return res;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true) {
            StringTokenizer size = new StringTokenizer(br.readLine());
            L = Integer.parseInt(size.nextToken());
            R = Integer.parseInt(size.nextToken());
            C = Integer.parseInt(size.nextToken());
            
            if (L == 0 && R == 0 && C == 0) {
                break;
            }
            
            board = new int[L][R][C];
            check = new boolean[L][R][C];
            
            for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                    String line = br.readLine();
                    
                    for (int k = 0; k < C; k++) {
                        if (line.charAt(k) == 'S') {
                            S = new int[] {i, j, k};
                            board[i][j][k] = 0;
                        } else if (line.charAt(k) == 'E') {
                            E = new int[] {i, j, k};
                            board[i][j][k] = 0;
                        } else if (line.charAt(k) == '#') {
                            board[i][j][k] = 1;
                        } else {
                            board[i][j][k] = 0;
                        }
                    }
                }
                
                br.readLine();
            }
            
            int res = bfs();
            
            if (res == 0) {
            	System.out.println("Trapped!");
            } else {
            	System.out.println("Escaped in " + res + " minute(s).");
            }
        }
    }

}