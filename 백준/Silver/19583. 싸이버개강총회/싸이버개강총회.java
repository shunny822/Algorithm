import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().trim().split(" ");
		String S = input[0].replace(":", "");
		int start = Integer.parseInt(S);
		String E = input[1].replace(":", "");
		int end = Integer.parseInt(E);
		String Q = input[2].replace(":", "");
		int quit = Integer.parseInt(Q);

		HashMap<String, Integer> check = new HashMap<String, Integer>();
		int cnt = 0;

		while (true) {
			String line = br.readLine();
			
			if (line == null) {
				break;
			}
			
			StringTokenizer stringT = new StringTokenizer(line);
			String temp = stringT.nextToken().replace(":", "");
			int time = Integer.parseInt(temp);
			String name = stringT.nextToken();
			
			if (time > start) {
				if (check.containsKey(name) && time >= end && time <= quit) {
					cnt++;
					check.remove(name);
				}
				break;
			}
			check.put(name, 0);
		}
		

		while (true) {
			String line = br.readLine();
			
			if (line == null) {
				break;
			}
			
			StringTokenizer stringT = new StringTokenizer(line);
			String temp = stringT.nextToken().replace(":", "");
			int time = Integer.parseInt(temp);
			String name = stringT.nextToken();
			
			if (check.containsKey(name) && time >= end && time <= quit) {
				cnt++;
				check.remove(name);
			}
		}

		System.out.println(cnt);
	}

}