import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, A, B;
	static ArrayList<int[]>[] list;
	
	static int prim() {
		PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> -o[1]));
		boolean[] check = new boolean[N+1];
		check[A] = true;
		int maxWeight = Integer.MAX_VALUE;
		
		for (int[] next : list[A]) {
			pq.add(next);
		}
		
		while (!pq.isEmpty()) {
			int[] now = pq.poll();
			if (check[now[0]]) {
				continue;
			}
			
			check[now[0]] = true;
			maxWeight = Math.min(maxWeight, now[1]);
			
			if (now[0] == B) {
//				maxWeight = now[1];
				break;
			}
			
			for (int[] next : list[now[0]]) {
				if (!check[next[0]]) {
//					check[next[0]] = true;
					pq.add(next);
				}
			}
			
		}
		
		return maxWeight;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer size = new StringTokenizer(br.readLine());
		N = Integer.parseInt(size.nextToken());
		M = Integer.parseInt(size.nextToken());
		list = new ArrayList[N+1];
		
		for (int i = 0; i < N+1; i++) {
			list[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer input = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(input.nextToken());
			int b = Integer.parseInt(input.nextToken());
			int c = Integer.parseInt(input.nextToken());
			
			list[a].add(new int[] {b, c});
			list[b].add(new int[] {a, c});
		}
		
		StringTokenizer v = new StringTokenizer(br.readLine());
		A = Integer.parseInt(v.nextToken());
		B = Integer.parseInt(v.nextToken());
		
		System.out.println(prim());
	}
}