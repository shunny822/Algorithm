import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static StringBuilder sb = new StringBuilder();
	static int[] arr;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer size = new StringTokenizer(br.readLine());
		N = Integer.parseInt(size.nextToken());
		M = Integer.parseInt(size.nextToken());
		arr = new int[N+1];
		
		StringTokenizer input = new StringTokenizer(br.readLine());
		
		for (int i = 1; i < N+1; i++) {
			arr[i] = arr[i-1] + Integer.parseInt(input.nextToken());
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer numbers = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(numbers.nextToken());
			int b = Integer.parseInt(numbers.nextToken());
			
			sb.append(arr[b] - arr[a-1]).append("\n");
		}
		
		System.out.println(sb.toString());
	}

}