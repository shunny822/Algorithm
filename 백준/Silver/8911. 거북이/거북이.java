import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	private static int[] dy = {-1, 0, 1, 0};
	private static int[] dx = {0, 1, 0, -1};
	
	private static void move(int[] me, char order) {
		switch (order) {
		case 'F':
			me[0] += dy[me[2]];
			me[1] += dx[me[2]];
			break;
		case 'B':
			me[0] += dy[(me[2]+2)%4];
			me[1] += dx[(me[2]+2)%4];
			break;
		case 'L':
			me[2] = (me[2]+3)%4;
			break;
		case 'R':
			me[2] = (me[2]+1)%4;
		default:
			break;
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < t; i++) {
			int[] me = {0, 0, 0};
			int[] minPosition = {0, 0};
			int[] maxPosition = {0, 0};
			
			String order = br.readLine().trim();
			int l = order.length();
			
			for (int j = 0; j < l; j++) {
				move(me, order.charAt(j));
				
				if (me[0] < minPosition[0]) {
					minPosition[0] = me[0];
				} else if (me[0] > maxPosition[0]) {
					maxPosition[0] = me[0];
				}
				
				if (me[1] < minPosition[1]) {
					minPosition[1] = me[1];
				} else if (me[1] > maxPosition[1]) {
					maxPosition[1] = me[1];
				}
			}
			
			System.out.println((maxPosition[0]-minPosition[0]) * (maxPosition[1]-minPosition[1]));
		}
	}
}