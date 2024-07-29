import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	private static boolean checkCnt(int A, int C, int G, int T, HashMap<Character, Integer> cnt) {
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
		int A = Integer.parseInt(target.nextToken());
		int C = Integer.parseInt(target.nextToken());
		int G = Integer.parseInt(target.nextToken());
		int T = Integer.parseInt(target.nextToken());
		
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
		
		if (checkCnt(A, C, G, T, count)) {
			res++;
		}
		
		for (int i = P; i < S; i++) {
			char rmS = dna.charAt(i-P);
			count.replace(rmS, count.get(rmS)-1);
			char addS = dna.charAt(i);
			count.replace(addS, count.get(addS)+1);
			
			if (checkCnt(A, C, G, T, count)) {
				res++;
			}
		}
		System.out.println(res);
	}

}