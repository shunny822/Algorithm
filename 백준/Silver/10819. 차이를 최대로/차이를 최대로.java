import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	private static int getMax(int n, int[] arr) {
		int res = 0;
		
		for (int i = 0; i < n-1; i++) {
			res += Math.abs(arr[i] - arr[i+1]);
		}
		return res;
	}
	
	private static int findArr(int n, int[] newArr, int[] origin, boolean[] check, int idx, int res) {
		if (idx == n) {
			return getMax(n, newArr);
		}
		
		for (int i = 0; i < n; i++) {
			if (!check[i]) {
				check[i] = true;
				newArr[idx] = origin[i];
				res = Math.max(res, findArr(n, newArr, origin, check, idx+1, res));
				check[i] = false;
			}
		}
		return res;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer input = new StringTokenizer(br.readLine());
		int[] array = new int[N];
		
		for (int i = 0; i < N; i++) {
			array[i] = Integer.parseInt(input.nextToken());
		}
		
		int[] newArr = new int[N];
		boolean[] check = new boolean[N];
		System.out.println(findArr(N, newArr, array, check, 0, 0));
	}
}
