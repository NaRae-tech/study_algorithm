package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class how_many_circle_version3 {
	public static int gcd(int a, int b) {
		while(b!=0) {
			int n = a%b;
			a = b;
			b = n;
		}
		return a;
	}
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s ="";
		try {
			s = bf.readLine();
		} catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		int T = Integer.parseInt(st.nextToken());
		try {
			s = bf.readLine();
		}catch(IOException e) {}
        
		StringTokenizer sn = new StringTokenizer(s);
		int numbers[] = new int[T];
		for(int i =0;i<T;i++) {
			numbers[i] = Integer.parseInt(sn.nextToken());
		}
        
		StringBuilder answer = new StringBuilder();
		for(int i =1;i<T;i++) {
			int maximum = gcd(numbers[0], numbers[i]);
			answer.append((int)(numbers[0]/maximum));
			answer.append("/");
			answer.append((int)(numbers[i]/maximum));
			answer.append("\n");
		}
		System.out.println(answer);
	}
}
