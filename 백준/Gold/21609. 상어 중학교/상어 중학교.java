import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N, M, score;
    private static int[][] arr;
    private static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    private static class Block {
        int y;
        int x;
        List<int[]> elements = new ArrayList<>();
        int rainbowCnt = 0;

        Block(int y, int x) {
            this.y = y;
            this.x = x;
            this.elements.add(new int[] {y, x});
        }
    }

    private static Block makeBlock(int i, int j, boolean[][] normalBlockCheck) {
        int flag = arr[i][j];
        Block block = new Block(i, j);
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {i, j});
        boolean[][] check = new boolean[N][N];
        check[i][j] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (int[] d : delta) {
                int ny = now[0] + d[0];
                int nx = now[1] + d[1];

                if (ny >= 0 && ny < N && nx >= 0 && nx < N && !check[ny][nx] && (arr[ny][nx] == flag || arr[ny][nx] == 0)) {
                    check[ny][nx] = true;
                    q.offer(new int[] {ny, nx});
                    block.elements.add(new int[] {ny, nx});

                    if (arr[ny][nx] == 0) {
                        block.rainbowCnt++;
                    } else {
                        normalBlockCheck[ny][nx] = true;
                    }
                }
            }
        }

        return block;
    }

    private static void downBlock() {
        for (int x = 0; x < N; x++) {
            int downIdx = N-1;

            while (true) {
                while (downIdx > 0 && arr[downIdx][x] != -2) {
                    downIdx--;
                }

                if (downIdx == 0) {
                    break;
                }

                int findIdx = downIdx - 1;

                while (findIdx >= 0 && arr[findIdx][x] == -2) {
                    findIdx--;
                }

                if (findIdx < 0) {
                    break;
                } else if (arr[findIdx][x] == -1) {
                    downIdx = findIdx;
                } else {
                    arr[downIdx][x] = arr[findIdx][x];
                    arr[findIdx][x] = -2;
                }
            }
        }
    }

    private static void turnArr() {
        int[][] newArr = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                newArr[N-j-1][i] = arr[i][j];
            }
        }

        arr = newArr;
    }

    private static void autoPlay() {
        List<Block> list = new ArrayList<>();

        while(true) {
            list.clear();
            boolean[][] normalBlockCheck = new boolean[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (arr[i][j] > 0 && !normalBlockCheck[i][j]) {
                        normalBlockCheck[i][j] = true;
                        list.add(makeBlock(i, j, normalBlockCheck));
                    }
                }
            }

            list.sort((o1, o2) -> {
                if (o1.elements.size() != o2.elements.size()) {
                    return o2.elements.size() - o1.elements.size();
                }

                if (o1.rainbowCnt != o2.rainbowCnt) {
                    return o2.rainbowCnt - o1.rainbowCnt;
                }

                if (o1.y != o2.y) {
                    return o2.y - o1.y;
                }

                return o2.x - o1.x;
            });

            if (list.isEmpty() || list.get(0).elements.size() == 1) {
                break;
            }

            int blockSize = list.get(0).elements.size();
            score += blockSize * blockSize;

            for (int[] p : list.get(0).elements) {
                arr[p[0]][p[1]] = -2;
            }

            downBlock();
            turnArr();
            downBlock();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer size = new StringTokenizer(br.readLine());
        N = Integer.parseInt(size.nextToken());
        M = Integer.parseInt(size.nextToken());
        score = 0;
        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer nums = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(nums.nextToken());
            }
        }

        autoPlay();
        System.out.println(score);
    }

}