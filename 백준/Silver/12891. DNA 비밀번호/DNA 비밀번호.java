import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static int A, C, G, T;
	
	private static boolean checkCnt(HashMap<Character, Integer> cnt) {
		if (cnt.get('A') < A || cnt.get('C') < C || cnt.get('G') < G || cnt.get('T') < T) {
			return false;
		}
		return true;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer l = new StringTokenizer(br.readLine());
		int S = Integer.parseInt(l.nextToken());
		int P = Integer.parseInt(l.nextToken());
		
		String dna = br.readLine();
		
		StringTokenizer target = new StringTokenizer(br.readLine());
		A = Integer.parseInt(target.nextToken());
		C = Integer.parseInt(target.nextToken());
		G = Integer.parseInt(target.nextToken());
		T = Integer.parseInt(target.nextToken());
		
		HashMap<Character, Integer> count = new HashMap<>();
		count.put('A', 0);
		count.put('C', 0);
		count.put('G', 0);
		count.put('T', 0);
		
		for (int i = 0; i < P; i++) {
			char s = dna.charAt(i);
			count.replace(s, count.get(s)+1);
		}
		
		int res = 0;
		
		if (checkCnt(count)) {
			res++;
		}
		
		for (int i = P; i < S; i++) {
			char rmS = dna.charAt(i-P);
			count.replace(rmS, count.get(rmS)-1);
			char addS = dna.charAt(i);
			count.replace(addS, count.get(addS)+1);
			
			if (checkCnt(count)) {
				res++;
			}
		}
		System.out.println(res);
	}

}