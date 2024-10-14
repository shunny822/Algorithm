import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	private static int N;
	private static String[] phoneNumbers;
	private static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 1; t <= T; t++) {
        	N = Integer.parseInt(br.readLine());
        	phoneNumbers = new String[N];
        	
        	for (int i = 0; i < N; i++) {
        		phoneNumbers[i] = br.readLine();
        	}
        	
        	Arrays.sort(phoneNumbers);
        	boolean isPossible = true;
        	
        	for (int i = 0; i < N-1; i++) {
        		int l = phoneNumbers[i].length();
        		
        		if (phoneNumbers[i+1].length() >= l && phoneNumbers[i+1].substring(0, l).equals(phoneNumbers[i])) {
        			sb.append("NO\n");
        			isPossible = false;
        			break;
        		}
        	}
        	
        	if (isPossible) {
        		sb.append("YES\n");
        	}
        }
        
		System.out.println(sb.toString());
	}
	
}