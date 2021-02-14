package baekjoon;

import java.util.Scanner;

public class how_many_circle {
	public static int gcd(int a, int b) {
		while(b!=0) {
			int n = a%b;
			a = b;
			b = n;
		}
		return a;
	}
	public static void main(String[] args) {
		//입력받기
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int numbers[] = new int[T];
		for(int i =0;i<T;i++) {
			numbers[i] = sc.nextInt();
		}
		for(int i =1;i<T;i++) {
			int maximum = gcd(numbers[0], numbers[i]);
			System.out.println((int)(numbers[0]/maximum)+"/"+(int)(numbers[i]/maximum));
			
		}
	}
}