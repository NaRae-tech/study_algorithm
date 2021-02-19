package baekjoon;

import java.util.Scanner;
public class binomial_coefficient {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int count = K;
		
		long up = 1;
		long down = 1;
		while((count--)!=0) {
			up*=(N--);
			down*=(K--);
		}
		
		System.out.println((int)(up/down));
	}
}
