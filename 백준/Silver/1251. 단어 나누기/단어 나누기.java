import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	private static String switchStr(String str, int i1, int i2) {
		String str1 = str.substring(0, i1);
		String str2 = str.substring(i1, i2);
		String str3 = str.substring(i2, str.length());
		
		StringBuilder sb = new StringBuilder();
		sb.append(new StringBuilder(str1).reverse().toString());
		sb.append(new StringBuilder(str2).reverse().toString());
		sb.append(new StringBuilder(str3).reverse().toString());
		return sb.toString();
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine().trim();
		int l = input.length();
		ArrayList<String> arr = new ArrayList<>();
		
		for (int i = 1; i < l-1; i++) {
			for (int j = i+1; j < l; j++) {
				arr.add(switchStr(input, i, j));
			}
		}
		
		Collections.sort(arr);
		System.out.println(arr.get(0));
	}

}