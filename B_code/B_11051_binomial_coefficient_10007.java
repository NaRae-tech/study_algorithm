package baekjoon;

import java.util.Scanner;
public class binomial_coefficient_10007 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int num[][] = new int[N+1][N+1];
		
		for(int i =0;i<N+1;i++) {
			for(int j =0;j<=i;j++) {
				if((j==0)||(j==i)){
					num[i][j]=1;
				}
				else {
					num[i][j] = (num[i-1][j]%10007+num[i-1][j-1]%10007)%10007;
				}
			}
		}
		
		System.out.println(num[N][K]%10007);
	}
}