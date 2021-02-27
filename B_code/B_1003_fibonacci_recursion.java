package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
public class fibonacci_recursion {
	
	static int zero =0;
	static int one = 0;
	
	public static int fibonacci(int i) {
		if (i==0) {
			zero+=1;
			return 0;
		}
		else if(i==1) {
			one+=1;
			return 1;
		}
		else return fibonacci(i-1)+fibonacci(i-2);
	}
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb= new StringBuilder();
		try {
			int N = Integer.parseInt(bf.readLine());
			for (int n = 0;n<N;n++) {
				try {
					zero=0;
					one=0;
					
					int a = Integer.parseInt(bf.readLine());
					int answer = fibonacci(a);
					sb.append(zero+" "+one+"\n");
				} catch(IOException e) {}
			}
			System.out.println(sb);
		} catch(IOException e) {}
	}
}
