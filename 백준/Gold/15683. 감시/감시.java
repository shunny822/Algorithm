import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] office;
    static int[][] delta = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static ArrayList<int[]>[] deltaIdx;
    static ArrayList<int[]> cctv;
    static int res = Integer.MAX_VALUE;

    static void setDeltaIdx() {
        deltaIdx = new ArrayList[6];

        for (int i = 0; i <= 5; i++) {
            deltaIdx[i] = new ArrayList<int[]>();
        }

        for (int i = 0; i < 4; i++) {
            int[] idx = { i };
            deltaIdx[1].add(idx);
        }

        for (int i = 0; i < 2; i++) {
            int[] idx = { i, (i + 2) % 4 };
            deltaIdx[2].add(idx);
        }

        for (int i = 0; i < 4; i++) {
            int[] idx = { i, (i + 1) % 4 };
            deltaIdx[3].add(idx);
        }

        for (int i = 0; i < 4; i++) {
            int[] idx = { i, (i + 1) % 4, (i + 2) % 4 };
            deltaIdx[4].add(idx);
        }

        int[] idx = { 0, 1, 2, 3 };
        deltaIdx[5].add(idx);
    }

    static void makeDir(int idx, int[] cctvDir) {
        if (idx == cctv.size()) {
            cntBlindZone(cctvDir);
            return;
        }

        int[] position = cctv.get(idx);
        int cctvNumber = office[position[0]][position[1]];

        for (int i = 0; i < deltaIdx[cctvNumber].size(); i++) {
            cctvDir[idx] = i;
            makeDir(idx + 1, cctvDir);
        }
    }

    static void cntBlindZone(int[] cctvDir) {
        boolean[][] show = new boolean[N][M];

        for (int i = 0; i < cctv.size(); i++) {
            int[] position = cctv.get(i);
            show[position[0]][position[1]] = true;
            int cctvNumber = office[position[0]][position[1]];
            int[] deltaValues = deltaIdx[cctvNumber].get(cctvDir[i]);

            for (int d : deltaValues) {
            	int originY = position[0];
            	int originX = position[1];
                int dy = delta[d][0];
                int dx = delta[d][1];
                
                while (true) {
                    int ny = originY + dy;
                    int nx = originX + dx;
                    
                    if (ny < 0 || ny >= N || nx < 0 || nx >= M || office[ny][nx] == 6) {
                        break;
                    }
                    
                    show[ny][nx] = true;
                    originY = ny;
                    originX = nx;
                }
            }
        }

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (office[i][j] == 0 && !show[i][j]) {
                    cnt++;
                }
            }
        }

        res = Math.min(res, cnt);
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer size = new StringTokenizer(br.readLine());

        setDeltaIdx();
        N = Integer.parseInt(size.nextToken());
        M = Integer.parseInt(size.nextToken());
        office = new int[N][M];
        cctv = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer line = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                office[i][j] = Integer.parseInt(line.nextToken());

                if (office[i][j] != 0 && office[i][j] != 6) {
                    int[] p = { i, j };
                    cctv.add(p);
                }
            }
        }

        makeDir(0, new int[cctv.size()]);
        System.out.println(res);
    }
}