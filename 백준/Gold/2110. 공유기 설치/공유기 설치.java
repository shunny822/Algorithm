import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N, C;
    private static int[] house;
    
    private static int calcMinDist(int interval) {
        int prev = house[0];
        int wifi = 1;
        
        for (int i = 1; i < N; i++) {
        	if (house[i] - prev >= interval) {
        		prev = house[i];
        		wifi++;
        		
        		if (wifi == C) {
        			break;
        		}
        	}
        }
        
        return wifi;
    }
    
    private static int binarySearch() {
        int s = 0;
        int e = house[N-1];
        int res = 0;
        
        while (s <= e) {
            int mid = (s + e) / 2;
            int temp = calcMinDist(mid);
            
            if (temp < C) {
            	e = mid - 1;
            } else {
            	res = Math.max(res, mid);
            	s = mid + 1;
            }
        }
        
        return res;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nums = new StringTokenizer(br.readLine());
        N = Integer.parseInt(nums.nextToken());
        C = Integer.parseInt(nums.nextToken());
        house = new int[N];
        
        for (int i = 0; i < N; i++) {
            int h = Integer.parseInt(br.readLine());
            house[i] = h;
        }
        
        Arrays.sort(house);
        System.out.println(binarySearch());
    }

}