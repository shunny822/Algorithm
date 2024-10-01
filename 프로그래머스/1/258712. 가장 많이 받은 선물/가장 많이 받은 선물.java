import java.util.*;

class Solution {
    private static int l;
    private static HashMap<String, Integer> friendIdx = new HashMap<>();
    private static int[][] giveAndTake;
    private static int[] giftDegree;
    
    private static void cntGiveAndTake(String[] gifts) {
        for (String gift : gifts) {
            String[] f = gift.split(" ");
            int giverIdx = friendIdx.get(f[0]);
            int takerIdx = friendIdx.get(f[1]);
            giveAndTake[giverIdx][takerIdx]++;
        }
    }
    
    private static void calcGiftDegree() {
        for (int i = 0; i < l; i++) {
            int give = 0;
            for (int j = 0; j < l; j++) {
                give += giveAndTake[i][j];
            }
            
            int take = 0;
            for (int j = 0; j < l; j++) {
                take += giveAndTake[j][i];
            }
            
            giftDegree[i] = give - take;
        }
    }
    
    private static int findMax() {
        int[] toGet = new int[l];
        
        for (int f1 = 0; f1 < l; f1++) {
            for (int f2 = f1+1; f2 < l; f2++) {
                int v1 = giveAndTake[f1][f2];
                int v2 = giveAndTake[f2][f1];
                
                if (v1 < v2) {
                    toGet[f2]++;
                } else if (v2 < v1) {
                    toGet[f1]++;
                } else {
                    if (giftDegree[f1] > giftDegree[f2]) {
                        toGet[f1]++;
                    } else if (giftDegree[f2] > giftDegree[f1]) {
                        toGet[f2]++;
                    }
                }
            }
        }
        
        int res = 0;
        for (int v : toGet) {
            res = Math.max(res, v);
        }
        
        return res;
    }
    
    public int solution(String[] friends, String[] gifts) {
        l = friends.length;
        giveAndTake = new int[l][l];
        giftDegree = new int[l];
        
        for (int i = 0; i < l; i++) {
            friendIdx.put(friends[i], i);
        }
        
        cntGiveAndTake(gifts);
        calcGiftDegree();
        
        return findMax();
    }
}