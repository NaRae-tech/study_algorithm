package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer; 

public class N_and_M_3 {
	static int arr[] = new int[8];
	//static boolean check[] = new boolean[8];
	public static void function(int index, int N, int M, StringBuilder sb) {
		if(index==M) {
			for(int i =0;i<M;i++) {
				sb.append(arr[i]);
				if(i!=M-1){sb.append(' ');}
			}
			sb.append("\n");
		}
		else {
			for(int i = 1;i<=N;i++) {
				arr[index] = i;
				//check[i] = true;
				function(index+1,N,M,sb);
				//check[i] = false;
			}
		}
	}
	public static void main(String[] as) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		StringBuilder sb = new StringBuilder();
		try {
			s = bf.readLine();
		} catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		function(0,N,M,sb);
		System.out.println(sb);
	}
}
