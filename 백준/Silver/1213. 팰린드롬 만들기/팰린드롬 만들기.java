import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int[] count = new int[26];
		
		for (int i = 0; i < input.length(); i++) {
			count[input.charAt(i)-'A']++;
		}
		
		int oddCnt = 0;
		int oddIdx = -1;
		
		for (int i = 0; i < count.length; i++) {
			if (count[i] > 0 && count[i]%2 != 0) {
				oddCnt++;
				oddIdx = i;
			}
		}
		
		if (oddCnt > 1) {
			System.out.println("I'm Sorry Hansoo");
		} else {
			StringBuilder res = new StringBuilder();
			
			for (int i = 0; i < 26; i++) {
				for (int j = 0; j < count[i]/2; j++) {
					res.append((char) (i+'A'));
				}
			}
			
			String temp = res.toString();
			
			if (oddIdx != -1) {
				res.append((char) (oddIdx+'A'));
			}
			
			for (int i = temp.length()-1; i >= 0; i--) {
				res.append(temp.charAt(i));
			}
			
			System.out.println(res.toString());
		}
		
	}
}
