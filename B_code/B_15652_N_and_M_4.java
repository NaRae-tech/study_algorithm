package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class N_and_M_4 {
	static int arr[] = new int[9];
	public static void function(int index, int N, int M, StringBuilder sb) {
		if(index==M+1) {
			for(int i =1;i<=M;i++) {
				sb.append(arr[i]);
				if(i!=M) {sb.append(' ');}
			}
			sb.append("\n");
		}
		else {
			for(int i=1;i<=N;i++) {
				if(arr[index-1]<=i) {
					arr[index]=i;
					function(index+1, N,M,sb);
				}
			}
		}
	}
	public static void main(String[] as) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		StringBuilder sb = new StringBuilder(s);
		try {s=bf.readLine();} catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		function(1,N,M,sb);
		System.out.println(sb);		
	}
}
