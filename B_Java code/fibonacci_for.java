package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class fibonacci_for {

	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb= new StringBuilder();
		try {
			int N = Integer.parseInt(bf.readLine());
			for(int i =0;i<N;i++) {
				try {
					int target = Integer.parseInt(bf.readLine());
					
					int list[][] = new int[41][2];
					list[0][0] = 1;
					list[0][1] = 0;
					list[1][0] = 0;
					list[1][1] = 1;
					
					for(int j = 2;j<=target;j++) {
						list[j][0] = list[j-1][0]+list[j-2][0];
						list[j][1] = list[j-1][1]+list[j-2][1];
					}
					
					sb.append(list[target][0]+" "+ list[target][1]+"\n");
				}
				catch(IOException e) {}
			}
			System.out.println(sb);
		}
		catch(IOException e) {}
	}
}
