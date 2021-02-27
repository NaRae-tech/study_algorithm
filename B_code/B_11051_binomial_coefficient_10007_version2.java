package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class binomial_coefficient_10007_version2 {
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s= "";
		try {
			s= bf.readLine();
		}catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int num[][] = new int[N+1][N+1];
		for(int i =0;i<N+1;i++) {
			for(int j =0;j<=i;j++) {
				if(j==0||j==i) {
					num[i][j] = 1;
				}
				else {
					num[i][j] = (num[i-1][j-1]%10007+num[i-1][j]%10007)%10007;
				}
			}
		}
		System.out.println(num[N][K]);
	}
}
