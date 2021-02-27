package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class coin_0 {
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		try {
			s = bf.readLine();
		}catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int money[] = new int[N];
		for(int i =0;i<N;i++) {
			try {
				s = bf.readLine();
			}catch(IOException e) {}
			money[i] = Integer.parseInt(s);
		}
		Arrays.sort(money);
		
		int count =0;
		for(int i =N-1;i>=0;i--) {
			while(true) {
				if(K>=money[i]) {
					++count;
					K-=money[i];
				}
				else {
					break;
				}
			}
		}
		System.out.println(count);
	}
}
