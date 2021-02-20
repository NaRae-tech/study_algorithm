package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class ATM {

	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		try {
			s= bf.readLine();
		}catch(IOException e) {}
		int N = Integer.parseInt(s);
		
		int numbers[] = new int[N];
		try {
			s= bf.readLine();
		}catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		for(int i =0;i<N;i++) {
			numbers[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(numbers);
		int result = 0;
		for(int i =0;i<N;i++) {
			for (int j =0;j<=i;j++) {
				result+=numbers[j];
			}
		}
		System.out.println(result);
	}
}
