import java.util.*;

class Solution {
    private static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private static char seat = 'P';
    private static char partition = 'X';
    
    private static int bfs(String[] place, int y, int x) {
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] check = new boolean[5][5];
        q.offer(new int[] {y, x, 0});
        check[y][x] = true;
        
        while (!q.isEmpty()) {
            int[] now = q.poll();
            
            if (now[2] == 3) {
                break;
            }
            
            if (now[2] > 0 && now[2] <= 2 && place[now[0]].charAt(now[1]) == seat) {
                return 0;
            }
            
            for (int[] d : delta) {
                int ny = now[0] + d[0];
                int nx = now[1] + d[1];
                
                if (ny >= 0 && ny < 5 && nx >= 0 && nx < 5 && !check[ny][nx] && place[ny].charAt(nx) != partition) {
                    q.offer(new int[] {ny, nx, now[2]+1});
                    check[ny][nx] = true;
                }
            }
        }
        return 1;
    }
    
    private static int explore(String[] place) {
        for (int y = 0; y < 5; y++) {
            for (int x = 0; x < 5; x++) {
                if (place[y].charAt(x) == seat) {
                    int res = bfs(place, y, x);

                    if (res == 0) {
                        return 0;
                    }
                }
            }
        }
        
        return 1;
    }
    
    public int[] solution(String[][] places) {
        int[] ans = new int[5];
        
        for (int i = 0; i < 5; i++) {
            ans[i] = explore(places[i]);
        }
        
        return ans;
    }
}