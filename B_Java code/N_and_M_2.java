package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class N_and_M_2 {
	//조건에 맞는 수열
	static int arr[] = new int[9];
	//해당 숫자가 이미 수열에 포함됐는지 확인
	static boolean check[] = new boolean[9];
	 
	public static void function(int now, int index, int N, int M, StringBuilder sb) {
		if (index == M+1) {
			for(int i =1;i<=M;i++) {
				sb.append(arr[i]);
				if(i!=M) {
					sb.append(' ');
				}
			}
			sb.append("\n");
		}
		else {
			for(int i = now; i<=N;i++) {
				if(check[i]==true) {continue;}
				else if(arr[index-1]<i){
					arr[index] = i;
					check[i] = true;
					function(now,index+1,N,M,sb);
					check[i] = false;
					now++;
				}
			}
		}
	}
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		StringBuilder sb = new StringBuilder();
		try {
			s= bf.readLine();
		}catch (IOException e){}
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		function(1,1,N,M,sb);
		System.out.println(sb);
	}
}
