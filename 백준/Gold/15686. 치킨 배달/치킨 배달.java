import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
   private static void makeCombi(int m, int l, int idx, int before, ArrayList<int[]> combiArr, int[] arr, boolean[] check) {
      if (idx == m) {
         combiArr.add(Arrays.copyOf(arr, m));
         return;
      }

      for (int i = before+1; i < l; i++) {
         if (!check[i]) {
            check[i] = true;
            arr[idx] = i;
            makeCombi(m, l, idx+1, i, combiArr, arr, check);
            check[i] = false;
         }
      }
   }
   
   private static int calcChickenDistance(int y, int x, ArrayList<int[]> chickenStores, int[] chickenCombi) {
	   int res = (int) 1e9;
	   
	   for (int i : chickenCombi) {
		   int[] position = chickenStores.get(i);
		   res = Math.min(res, Math.abs(y-position[0]) + Math.abs(x-position[1]));
	   }
	   
	   return res;
   }

   private static int getMinDistance(int[][] city, ArrayList<int[]> chickenStores, int[] chickenCombi) {
      int res = 0;
      int l = city.length;
      
      for (int i = 0; i < l; i++) {
    	  for (int j = 0; j < l; j++) {
    		  if (city[i][j] == 1) {
    			  res += calcChickenDistance(i, j, chickenStores, chickenCombi);
    		  }
    	  }
      }
      
      return res;
   }

   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

      StringTokenizer nums = new StringTokenizer(br.readLine());
      int N = Integer.parseInt(nums.nextToken());
      int M = Integer.parseInt(nums.nextToken());
      int[][] city = new int[N][N];
      ArrayList<int[]> chickenStores = new ArrayList<>();

      for (int i = 0; i < N; i++) {
         StringTokenizer line = new StringTokenizer(br.readLine());

         for (int j = 0; j < N; j++) {
            int temp = Integer.parseInt(line.nextToken());
            city[i][j] = temp;

            if (temp == 2) {
               int[] chicken = {i, j};
               chickenStores.add(chicken);
            }
         }
      }
            
      ArrayList<int[]> chickenCombi = new ArrayList<>();
      int[] arr = new int[M];
      boolean[] check = new boolean[chickenStores.size()];

      makeCombi(M, chickenStores.size(), 0, -1, chickenCombi, arr, check);
     
      int ans = (int) 1e9;
      for (int[] combi : chickenCombi) {
    	  ans = Math.min(ans, getMinDistance(city, chickenStores, combi));
      }

      System.out.println(ans);
   }

}