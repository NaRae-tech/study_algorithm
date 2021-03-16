package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class B_11054_bytonic_sequence {
	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s="";
		try {s=bf.readLine();}catch(IOException e) {}
		int N = Integer.parseInt(s);
		try {s=bf.readLine();} catch(IOException e) {}
		StringTokenizer st = new StringTokenizer(s);
		ArrayList<Integer> number = new ArrayList<Integer>();
		for(int i =0;i<N;i++) {
			number.add(Integer.parseInt(st.nextToken()));
		}
		
		//0~N-1순으로 dq
		ArrayList<Integer> dq = new ArrayList<Integer>();
		for(int i =0;i<N;i++) {
			dq.add(1);
		} 
		for(int i =0;i<N;i++) {
			for(int j = 0;j<i;j++) {
				if(number.get(i)>number.get(j)) {
					dq.set(i, Math.max(dq.get(i),dq.get(j)+1));
				}
			}
		}
		
		//N-1~0순으로 dq
		ArrayList<Integer> dq2 = new ArrayList<Integer>();
		for(int i =0;i<N;i++) {
			dq2.add(1);
		} 
		for(int i =N-1;i>=0;i--) {
			for(int j = N-1;j>i;j--) {
				if(number.get(i)>number.get(j)) {
					dq2.set(i, Math.max(dq2.get(i),dq2.get(j)+1));
				}
			}
		}
		
		//양방향을 모두 고려한 결과
		ArrayList<Integer> dq3 = new ArrayList<Integer>();
		for(int i =0;i<N;i++) {
			dq3.add(1);
		}
		int max = 0;
		int maxInd = 0;
		for(int i =0;i<N;i++) {
			dq3.set(i, dq.get(i)+dq2.get(i));
			if(dq3.get(i)>max) {
				max = dq3.get(i);
				maxInd = i;
			}
		}
		
		System.out.println(max-1);
	}
}
