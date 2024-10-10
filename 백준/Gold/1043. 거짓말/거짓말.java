import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	private static int N, M, cnt;
	private static int[] root;
	private static HashSet<Integer> truth = new HashSet<>();
	
	private static int find(int num) {
		if (num == root[num]) {
			return num;
		}
		return root[num] = find(root[num]);
	}
	
	private static void union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		
		if (truth.contains(aRoot)) {
			root[bRoot] = aRoot;
		} else if (truth.contains(bRoot)) {
			root[aRoot] = bRoot;
		} else {
			root[bRoot] = aRoot;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer nums = new StringTokenizer(br.readLine());
		N = Integer.parseInt(nums.nextToken());
		M = Integer.parseInt(nums.nextToken());
		cnt = 0;
		root = new int[N+1];
		
		for (int i = 0; i <= N; i++) {
			root[i] = i;
		}
		
		nums = new StringTokenizer(br.readLine());
		int t = Integer.parseInt(nums.nextToken());
		
		for (int i = 0; i < t; i++) {
			truth.add(Integer.parseInt(nums.nextToken()));
		}
		
		int[] party = new int[M];
		
		for (int i = 0; i < M; i++) {
			nums = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(nums.nextToken());
			int a = Integer.parseInt(nums.nextToken());
			party[i] = a;
			
			for (int j = 0; j < n-1; j++) {
				int b = Integer.parseInt(nums.nextToken());
				union(a, b);
				a = b;
			}
		}
		
		for (int p : party) {
			if (truth.contains(find(p))) {
				cnt++;
			}
		}
		
		System.out.println(M - cnt);
	}

}