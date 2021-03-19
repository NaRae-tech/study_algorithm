package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class B_9251_LCS {
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String a= "";
		String b ="";
		try {a=bf.readLine();} catch(IOException e) {}
		try {b=bf.readLine();} catch(IOException e) {}
		char[] A = a.toCharArray();
		char[] B = b.toCharArray();
		
		int[][] dq = new int[1001][1001];
		for(int i =0;i<=A.length;i++) {
			dq[0][i] = 0;
		}
		for(int i =0;i<=B.length;i++) {
			dq[i][0] = 0;
		}
		
		for(int i = 1;i<=A.length;i++) {
			for(int j = 1;j<=B.length;j++) {
				if(A[i-1]==B[j-1]) {
					dq[i][j] = dq[i-1][j-1]+1;
				}
				else {
					dq[i][j] = Math.max(dq[i-1][j], dq[i][j-1]);
				}
			}
		}
		System.out.println(dq[A.length][B.length]);
	}
}