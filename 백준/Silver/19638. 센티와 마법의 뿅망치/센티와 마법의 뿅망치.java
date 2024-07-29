import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer input = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(input.nextToken());
		int H = Integer.parseInt(input.nextToken());
		int T = Integer.parseInt(input.nextToken());
		double one = 1;
		
		PriorityQueue<Double> people = new PriorityQueue<>(Collections.reverseOrder());
		
		for (int i = 0; i < N; i++) {
			people.add(Double.parseDouble(br.readLine()));
		}
		
		int cnt = 0;
		
		for (int t = 0; t < T; t++) {
			double height = people.poll();
			
			if (height < H) {
				System.out.println("YES\n" + cnt);
				return;
			}
			
			if (height <= 1) {
				people.add(height);
			} else {
				people.add(height/2);
			}
			
			cnt++;
		}
		
		double biggest = people.poll();
		
		if (biggest < H) {
			System.out.println("YES\n" + cnt);
		} else {
			System.out.println("NO\n" + (int) biggest);
		}
		
	}
}
