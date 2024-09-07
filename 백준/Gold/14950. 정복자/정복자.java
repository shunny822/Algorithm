import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N, M, t;
    static ArrayList<int[]>[] list;
    static int[] dist;
    
    static int prim() {
    	PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
    	boolean[] check = new boolean[N+1];
    	check[1] = true;
    	int totalPrice = 0;
    	int additionalCost = 0;
    	
    	for (int[] next : list[1]) {
    		pq.add(next);
    	}
    	
    	while (!pq.isEmpty()) {
    		int[] now = pq.poll();
    		
    		if (check[now[0]]) {
    			continue;
    		}
    		
    		check[now[0]] = true;
    		totalPrice += now[1] + additionalCost;
    		additionalCost += t;
    		
    		for (int[] next : list[now[0]]) {
    			if (!check[next[0]]) {
    				pq.add(next);
    			}
    		}
    	}
    	return totalPrice;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nums = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(nums.nextToken());
        M = Integer.parseInt(nums.nextToken());
        t = Integer.parseInt(nums.nextToken());
        list = new ArrayList[N+1];
        dist = new int[N+1];
        
        for (int i = 0; i < N+1; i++) {
        	list[i] = new ArrayList<>();
        }
        
        for (int i = 2; i < N+1; i++) {
        	dist[i] = Integer.MAX_VALUE;
        }
        
        for (int i = 0; i < M; i++) {
        	StringTokenizer input = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(input.nextToken());
            int b = Integer.parseInt(input.nextToken());
            int c = Integer.parseInt(input.nextToken());
            
            list[a].add(new int[] {b, c});
            list[b].add(new int[] {a, c});
        }
        
        System.out.println(prim());
    }
}