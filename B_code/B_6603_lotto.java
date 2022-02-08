package study.myself;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_6603_lotto {
	static int k;
	static int[] numbers;
	static int[] picked;
	
	public static void check(int cnt, int start) {
		if(cnt == 6) {
			for(int i =0;i<6;i++) {
				System.out.print(picked[i]+" ");
			}
			System.out.println();
			return;
		}
		for(int i=start;i<k;i++) {
			picked[cnt] = numbers[i];
			check(cnt+1, i+1);
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		while(true) {
			st = new StringTokenizer(br.readLine()," ");
			k=Integer.parseInt(st.nextToken());
			if(k==0) break;
			
			numbers = new int[k];
			for(int i =0;i<k;i++) {
				numbers[i] = Integer.parseInt(st.nextToken());
			}
			
			picked = new int[6];
			check(0,0);
			System.out.println();
		}
	}

}
