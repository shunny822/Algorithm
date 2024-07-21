import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	private static void changeByFemale(int[] array, int num) {
		num--;
		int l = array.length;
		int cnt = 0;
		
		while(true) {
			int temp = cnt+1;
			
			if (num+temp >= l | num-temp < 0) {
				break;
			}
			
			if (array[num-temp] == array[num+temp]) {
				cnt++;
			} else {
				break;
			}
		}
		
		for (int i = num-cnt; i < num+cnt+1; i++) {
			if (array[i] == 1) {
				array[i] = 0;
			} else {
				array[i] = 1;
			}
		}
	}
	
	private static void changeByMale(int[] array, int num) {
		int temp = num;
		int l = array.length;
		
		while (temp <= l) {
			if (array[temp-1] == 1) {
				array[temp-1] = 0;
			} else {
				array[temp-1] = 1;
			}
			
			temp += num;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] buttons = new int[n];
		
		for (int i = 0; i < n; i++) {
			buttons[i] = Integer.parseInt(st.nextToken());
		}
		
		int studentNum = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < studentNum; i++) {
			StringTokenizer input = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(input.nextToken());
			int switchNum = Integer.parseInt(input.nextToken());
			
			if (s == 1) {
				changeByMale(buttons, switchNum);
			} else {
				changeByFemale(buttons, switchNum);
			}
		}
		
		for (int j = 0; j < n; j += 20) {
			StringBuilder sb = new StringBuilder();
			
			for (int i = j; i < j + 20; i++) {
				if (i >= n) {
					break;
				}
				sb.append(Integer.toString(buttons[i])).append(" ");
			}
			
			System.out.println(sb);
		}
	}
}