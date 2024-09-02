import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int V, E, S;
    static int[] dist;
    static ArrayList<int[]>[] list;
    static PriorityQueue<int[]> pq;

    static void dijkstra() {
    	pq = new PriorityQueue<>(Comparator.comparing(o -> o[1]));
    	pq.add(new int[] {S, 0});
    	
    	while (!pq.isEmpty()) {
    		int[] now = pq.poll();
    		
    		if (dist[now[0]] < now[1]) {
    			continue;
    		}
    		
    		for (int[] next : list[now[0]]) {
    			int cost = now[1] + next[1];
    			
    			if (cost < dist[next[0]]) {
    				dist[next[0]] = cost;
    				pq.add(new int[] {next[0], cost});
    			}
    		}
    	}
    	
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nums = new StringTokenizer(br.readLine());
        V = Integer.parseInt(nums.nextToken());
        E = Integer.parseInt(nums.nextToken());
        S = Integer.parseInt(br.readLine());
        dist = new int[V+1];
        list = new ArrayList[V+1];
        
        for (int i = 0; i < V+1; i++) {
        	dist[i] = Integer.MAX_VALUE;
        }
        dist[S] = 0;
        
        for (int i = 0; i < V+1; i++) {
        	list[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < E; i++) {
        	StringTokenizer input = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(input.nextToken());
        	int b = Integer.parseInt(input.nextToken());
        	int c = Integer.parseInt(input.nextToken());
        	
        	list[a].add(new int[] {b, c});
        }
        
        dijkstra();
        StringBuilder sb = new StringBuilder();
        
        for (int i = 1; i < V+1; i++) {
        	if (dist[i] == Integer.MAX_VALUE) {
        		sb.append("INF").append("\n");
        	} else {
        		sb.append(dist[i]).append("\n");
        	}
        }
        
        System.out.println(sb.toString());
    }
}