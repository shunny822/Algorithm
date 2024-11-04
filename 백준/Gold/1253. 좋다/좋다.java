import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	private static int N, res;
	private static int[] arr;
	private static boolean[] check;
	
	private static void binarySearch(int findNum, int i, int j) {
		int s = 0;
		int e = N-1;
		int idx = -1;
		
		while(s <= e) {
			int mid = (s+e)/2;
			int temp = arr[mid];
			
			if (temp >= findNum) {
				idx = mid;
				e = mid-1;
			} else {
				s = mid+1;
			}
		}

		while(idx != -1 && idx < N && !check[idx] && arr[idx] == findNum) {
			if (idx != i && idx != j) {
				check[idx] = true;
				res++;
			}
			idx++;				
		}
	}
	
	private static void findGood() {
		for (int i = 0; i < N-1; i++) {
			for (int j = i+1; j < N; j++) {
				int temp = arr[i] + arr[j];
				binarySearch(temp, i, j);
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		res = 0;
		arr = new int[N];
		check = new boolean[N];
		
		StringTokenizer nums = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(nums.nextToken());
		}
		
		Arrays.sort(arr);
		findGood();
		System.out.println(res);
	}

}