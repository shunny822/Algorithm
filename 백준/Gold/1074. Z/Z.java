import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, r, c;
	static int cnt = 0;
	
	static void find(int l) {
		if (l == 1) {
			return;
		}

		int halfL = l/2;
		int quater = l*l/4;
		
		if (r < halfL) {
			if (c < halfL) {
			} else {
				c -= halfL;
				cnt += quater;
			}
		} else {
			if (c < halfL) {
				r -= halfL;
				cnt += quater*2;
			} else {
				r -= halfL;
				c -= halfL;
				cnt += quater*3;
			}
		}
		
		find(halfL);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new  BufferedReader(new InputStreamReader(System.in));
		StringTokenizer input = new StringTokenizer(br.readLine());
		N = (int) Math.pow(2, Integer.parseInt(input.nextToken()));
		r = Integer.parseInt(input.nextToken());
		c = Integer.parseInt(input.nextToken());
		
		find(N);
		System.out.println(cnt);
	}
	
}