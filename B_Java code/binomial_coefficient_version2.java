package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
public class binomial_coefficient_version2 {

	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		try {
			s = bf.readLine();
		}catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int count = K;
		
		int up =1;
		int down =1;
		while((count--)!=0) {
			up*=(N--);
			down*=(K--);
		}
		
		System.out.println((int)(up/down));
		
	}
}
