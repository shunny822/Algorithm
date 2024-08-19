import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	static int N;
	static String formula;
	static int operators;
	static int ans = Integer.MIN_VALUE;
	
	static int calc(int a, int b, String operator) {
		if (operator.equals("+")) {
			return a + b;
		} else if (operator.equals("-")) {
			return a - b;
		} else {
			return a * b;
		}
	}
	
	static void calcFormula(boolean[] check) {
		ArrayList<String> arr = new ArrayList<>();
		arr.add(Character.toString(formula.charAt(0)));
		int i = 1;
		
		while (i < N) {
			if (i%2 == 1 && check[(int) (i/2)]) {
				int a = Integer.parseInt(arr.get(arr.size()-1));
				int b = formula.charAt(i+1) - '0';
				int temp = calc(a, b, Character.toString(formula.charAt(i)));
				arr.set(arr.size()-1, Integer.toString(temp));
				i += 2;
			} else {
				arr.add(Character.toString(formula.charAt(i)));
				i++;
			}
		}
		int res = Integer.parseInt(arr.get(0));
		
		for (int j = 1; j < arr.size(); j+= 2) {
			res = calc(res, Integer.parseInt(arr.get(j+1)), arr.get(j));
		}
		
		ans = Math.max(ans, res);
	}
	
	static void combi(int start, boolean[] check) {
		calcFormula(check);

		if (start >= operators) {
			return;
		}
		
		for (int i = start; i < operators; i++) {
			check[i] = true;
			combi(i+2, check);
			check[i] = false;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		formula = br.readLine();
		operators = (int) (formula.length()/2);
		
		boolean[] check = new boolean[operators];
		combi(0, check);
		System.out.println(ans);
	}

}