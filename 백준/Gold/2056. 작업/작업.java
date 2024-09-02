import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] time;
    static int[] result;
    static int[] indegree;
    static ArrayList<Integer>[] list;
    static Deque<Integer> q;
    
    static void topologySort() {
    	while (!q.isEmpty()) {
    		int now = q.poll();
    		
    		for (int next : list[now]) {
    			indegree[next] -= 1;
    			result[next] = Math.max(result[next], result[now]+time[next]);
    			
    			if (indegree[next] == 0) {
    				q.add(next);
    			}
    		}
    	}
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        time = new int[N];
        result = new int[N];
        indegree = new int[N];
        list = new ArrayList[N];
        q = new ArrayDeque<>();
        
        for (int i = 0; i < N; i++) {
        	list[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < N; i++) {
        	StringTokenizer input = new StringTokenizer(br.readLine());
        	time[i] = Integer.parseInt(input.nextToken());
        	result[i] = time[i];
        	indegree[i] = Integer.parseInt(input.nextToken());
        	
        	for (int k = 0; k < indegree[i]; k++) {
        		list[Integer.parseInt(input.nextToken())-1].add(i);
        	}
        	
        	if (indegree[i] == 0) {
        		q.add(i);
        	}
        }
        
        topologySort();
        
        int res = 0;
        for (int i = 0; i < N; i++) {
        	res = Math.max(res, result[i]);
        }
        
        System.out.println(res);
    }
}